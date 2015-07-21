#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
from urlparse import urljoin
import os
import exifread

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Image


class ImageScraper:
    def __init__(self):
        self.engine = create_engine('sqlite:///images.db', echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    # since we are ignoring SSL certificate errors with verify=False, we silence
    # the important yet annoying log messages
    requests.packages.urllib3.disable_warnings()

    def get_image_page(self, url):
        # grab the page for the original image size instead
        # the generic image page
        url += 'sizes/o'
        req = requests.get(url, verify=False)
        assert req.status_code == 200

        soup = BeautifulSoup(req.content)

        image_tag = soup.find('div', {'id': 'allsizes-photo'}).find('img')
        image_link = image_tag.get('src')

        if self.save_image(image_link):
            imageList.append(image_link)
            print image_link

    def save_image(self, url):
        SAVE_DIR = 'images'
        req = requests.get(url, verify=False)
        fname = req.request.path_url.split('/')[-1]

        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)
        with open(os.path.join(SAVE_DIR, fname), "wb") as content:
            content.write(req.content)

        if self.get_exif_data(os.path.join(SAVE_DIR, fname), url):
            return True
        else:
            # No EXIF data available :-(
            os.remove(os.path.join(SAVE_DIR, fname))
            return False

    def get_exif_data(self, fname, url):

        keys = ['GPS GPSLongitude',
                'GPS GPSLatitude',
                'EXIF ExifImageLength',
                'EXIF ExifImageWidth',
                'EXIF DateTimeOriginal']
        with open(fname, 'r') as fimage:
            tags = exifread.process_file(fimage)
            # make sure all the EXIF tags we need are stored in the image
            if set(keys).issubset(tags):
                image = Image(sourceUrl=url,
                              dateRetreived=datetime.datetime.now(),
                              latitude=str(tags['GPS GPSLatitude'].values),
                              longitude=str(tags['GPS GPSLongitude'].values),
                              imageDate=datetime.datetime.strptime(
                                  tags['EXIF DateTimeOriginal'].values,
                                  '%Y:%m:%d %H:%M:%S'
                              ),
                              imageHeight=tags['EXIF ExifImageLength'].values[0],
                              imageWidth=tags['EXIF ExifImageWidth'].values[0],
                              imageFile=url.split('/')[-1])

                # Add the new record to the DB session object
                self.session.add(image)

                return True
            else:
                return False

    def commitObject(self):
        self.session.commit()

    def closeSession(self):
        self.session.close()

    def main(self):

        url = 'https://www.flickr.com/search/?q=california&cm=apple%2Fiphone_5s'
        req = requests.get(url, verify=False)

        assert req.status_code == 200

        soup = BeautifulSoup(req.content, "html5lib")

        # get list of image URLs from search
        all_image_links = []
        for image_link in soup.find_all('a', {'class': 'title'}):
            # all_image_links.append(urljoin(req.request.url,
            # image_link.get('href')))
            all_image_links.append(urljoin(req.request.url, image_link.get('href')))
        images = set(all_image_links)

        # download images and process exif info
        for image in images:
            self.get_image_page(image)
            # print image


if __name__ == "__main__":
    imageList = []
    try:
        imageScraper = ImageScraper()
        imageScraper.main()
        imageScraper.session.commit()
    finally:
        # DB cleanup
        imageScraper.session.close()

    print('Image Count: {0}'.format(len(imageList)))
