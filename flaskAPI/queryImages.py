import table_def
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ImageReader:
    def __init__(self):
        self.session = sessionmaker()
        self.imageDef = table_def.Image
        self.engine = create_engine('sqlite:///flickrAPI/images.db', echo=True)
        self.session.configure(bind=self.engine)

    def query(self):
        s = self.session()
        self._results = s.query(self.imageDef).all()

    @property
    def results(self):
        return self._results
