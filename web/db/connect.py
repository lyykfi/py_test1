""" """
from contextlib import contextmanager

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

        Base.metadata.create_all(self.engine)

    def get_session(self):
        return sessionmaker(bind=self.engine)

    @contextmanager
    def session_scope(self):
        Session = self.get_session()
        session = Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()