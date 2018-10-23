""" """

import json_config
from singleton_decorator import singleton

@singleton
class DBSQL:
    def __init__(self):
        self.config = json_config.connect('./config/db.json')

    def get_sql_from_file(self, table, name):
        fd = open(self.config['sql_folder'] + table + '/' + name + '.sql', 'r')
        sql_data = fd.read()
        fd.close()

        return sql_data