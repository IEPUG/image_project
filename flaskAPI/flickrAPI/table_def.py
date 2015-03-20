# table_def.py
from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()

class Image(Base):
    __tablename__ = "images"
 
    id = Column(Integer, primary_key=True)
    sourceUrl = Column(String)
    dateRetreived = Column(Date)
    latitude = Column(String)
    longitude = Column(String)
    imageDate = Column(Date)
    imageWidth = Column(Integer)
    imageHeight = Column(Integer)
    imageFile = Column(String)

        
 
# create tables
engine = create_engine('sqlite:///images.db', echo=True)
Base.metadata.create_all(engine)
