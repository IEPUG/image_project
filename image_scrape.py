#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
from urlparse import urljoin
import os

#since we are ignoring SSL certificate errors with verify=False, we silence the important yet annoying log messages
requests.packages.urllib3.disable_warnings()


def get_image_page(url):
    url = url  + 'sizes/o'  # grab the page for the original image size
    req = requests.get(url, verify=False)
    assert req.status_code == 200

    soup = BeautifulSoup(req.content)

    image_tag = soup.find('div',{'id':'allsizes-photo'}).find('img')
    image_link = image_tag.get('src')
    imageList.append(image_link)
    print image_link
    save_image(image_link)


def save_image(url):
    SAVE_DIR = 'images'
    req = requests.get(url, verify=False)
    fname = req.request.path_url.split('/')[-1]
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    with open(os.path.join(SAVE_DIR, fname), "wb") as content:
        content.write(req.content)


def main():

    url = 'https://www.flickr.com/search/?q=california&cm=apple%2Fiphone_5s'
    req = requests.get(url, verify=False)

    assert req.status_code == 200

    soup = BeautifulSoup(req.content, "html5lib")

    #get list of image URLs from search
    all_image_links = []
    for image_link in soup.find_all('a', {'class':'title'}):
        # all_image_links.append(urljoin(req.request.url, image_link.get('href')))
        all_image_links.append(urljoin(req.request.url, image_link.get('href')))
    images = set(all_image_links)

    #download images and process exif info
    for image in images:
        get_image_page(image)
        # print image


if __name__ == "__main__":
    imageList = []
    main()
    print('Image Count: {0}'.format(len(imageList)))

