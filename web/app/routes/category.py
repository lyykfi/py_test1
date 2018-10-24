""" Category server resource """
import json
from functools import reduce

import falcon

from web.db.connect import DBConnector
from web.db.sql import DBSQL
from web.db.tables import DBTables


class CategoryResource(object):
    def on_get(self, req, resp):
        # init connector
        connector = DBConnector()
        # init db sql
        db_sql = DBSQL()

        sql_select = db_sql.get_sql_from_file(DBTables.CATEGORY.value, 'select')

        cursor = connector.connection.cursor()
        cursor.execute(sql_select)
        data = cursor.fetchall()
        cursor.close()

        data = reduce(list.__add__, map(list, data))
        print(data)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(data)