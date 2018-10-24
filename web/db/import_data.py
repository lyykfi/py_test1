""" """
from sqlalchemy.exc import SQLAlchemyError

from web.db.models.category import Category
from .connect import DBConnector
from web.aliexpress.request_parser.result import ParserRequestResult

class DBImport:
    def __init__(self):
        # init connector
        self.connector = DBConnector()

    def import_data(self, data: ParserRequestResult):
        session = self.connector.get_session()

        for category in data.categories:
            newCategory = Category(name=category.name)
            session.add(newCategory)
            try:
                session.commit()
            except SQLAlchemyError as error:
                session.rollback()
                print(error.args)


        session.close_all()
        return