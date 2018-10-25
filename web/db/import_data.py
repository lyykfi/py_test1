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
        with self.connector.session_scope() as session:
            session.add_all([Category(name=category.name) for category in data.categories])

            try:
                session.commit()
            except SQLAlchemyError as error:
                print(error.args)