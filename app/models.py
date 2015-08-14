from flask import current_app, request, url_for
from  . import db


class Image(db.Model):
    __tablename__ = 'images'
 
    id = db.Column(db.Integer, primary_key=True)
    sourceUrl = db.Column(db.String)
    dateRetreived = db.Column(db.Date)
    latitude = db.Column(db.String)
    longitude = db.Column(db.String)
    imageDate = db.Column(db.Date)
    imageWidth = db.Column(db.Integer)
    imageHeight = db.Column(db.Integer)
    imageFile = db.Column(db.String)

