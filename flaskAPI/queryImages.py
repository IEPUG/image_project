import table_def
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ImageReader:
    def __init__(self):
        self.session = sessionmaker()
        self.imageDef = table_def.Image
        self.engine = create_engine('sqlite:///flickrAPI/images.db', echo=True)
        self.session.configure(bind=self.engine)

    def queryAll(self):
        s = self.session()
        self._results = s.query(self.imageDef).all()

    def queryById(self, id):
        s = self.session()
        self._imageInfo = s.query(self.imageDef).filter(self.imageDef.id
                                                        == id).first()

    @property
    def results(self):
        return self._results

    @property
    def imageInfo(self):
        return self._imageInfo
