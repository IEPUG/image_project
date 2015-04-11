image_project
=============

*IEPUG Group Learning Project*


To install the module dependecies use the following (from within your virtual environment!):
```
# Scraping and ORM Modules
pip install requests
pip install beautifulsoup4
pip install html5lib
pip install exifread
pip install sqlalchemy

# Flickr and Flask Modules
pip install flickrapi
pip install flask
pip install flask-restful
```
Or use the requirements.txt file with pip:
```
pip install -r requirements.txt
```

Authentication
---------------
In order to pull images from the Flickr API, you need to first register as a developer at https://www.flickr.com/services/developer/api/

After you do that, with your favorite text editor, open flaskAPI/flickrAPI/config.ini, and insert your API key and secret that was given to you.

Additional Info
---------------
In general, the overall idea of this sample project is to scrape a bunch of images off of flickr from something like [this search](https://www.flickr.com/search/?q=california&cm=apple%2Fiphone_5s), extract some GPS EXIF info from the images, save the images to local storage, and insert some meta data into an sqlite database using SQLAlchemy.

Additional steps will be to do some GIS tasks with the GPS info we saved, and then create a web app using flask.  After that we can put the web service in the cloud.
