""" """
import json_config
from singleton_decorator import singleton
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

@singleton
class DBConnector:

    def __init__(self):
        self.config = json_config.connect('./config/db.json')
        self.engine = create_engine('sqlite:///'+self.config['db_file'], echo=True)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        Base.metadata.create_all(self.engine)