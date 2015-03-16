#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
from urlparse import urljoin
import re
import os


def get_image_page(url):
    req = requests.get(url, verify=False)
    assert req.status_code == 200

    soup = BeautifulSoup(req.content)

    for link in soup.find_all('img', 'main-photo'):
        image_link = link.get('src')
        imageList.append(image_link)
        print image_link
        # save_image(urljoin(req.request.url, image_link))


def save_image(url):
    SAVE_DIR = 'images'
    req = requests.get(url)
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
        all_image_links.append(urljoin(req.request.url, image_link.get('href')))
    images = set(all_image_links)

    #download images and process exif info
    for image in images:
        # get_image_page(image)
        print image


if __name__ == "__main__":
    imageList = []
    main()
    print('Image Count: {0}'.format(len(imageList)))

