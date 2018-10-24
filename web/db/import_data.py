""" """

from .connect import DBConnector
from web.aliexpress.request_parser.result import ParserRequestResult
from .sql import DBSQL
from .tables import DBTables

class DBImport:
    def __init__(self):
        # init connector
        self.connector = DBConnector()
        # init db sql
        self.db_sql = DBSQL()

    def import_data(self, data: ParserRequestResult):
        # drop table
        sql_drop = self.db_sql.get_sql_from_file(DBTables.CATEGORY.value, 'drop')
        self.connector.connection.execute(sql_drop)

        # create table
        sql_create = self.db_sql.get_sql_from_file(DBTables.CATEGORY.value, 'create')
        self.connector.connection.execute(sql_create)

        # insert data
        # create table
        sql_insert = self.db_sql.get_sql_from_file(DBTables.CATEGORY.value, 'insert')

        for category in data.categories:
            self.connector.connection.execute(sql_insert, [category.name])

        self.connector.connection.commit()
        return