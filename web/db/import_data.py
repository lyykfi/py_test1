""" """
from web.db.models.category import Category
from .connect import DBConnector
from web.aliexpress.request_parser.result import ParserRequestResult

class DBImport:
    def __init__(self):
        # init connector
        self.connector = DBConnector()

    def import_data(self, data: ParserRequestResult):
        self.connector.session.query(Category).delete()
        self.connector.session.commit()

        for category in data.categories:
            newCategory = Category(name=category.name)
            self.connector.session.add(newCategory)

        self.connector.session.commit()
        return