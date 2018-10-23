""" """
import sqlite3
import json_config
from singleton_decorator import singleton

@singleton
class DBConnector:
    def __init__(self):
        self.config = json_config.connect('./config/db.json')
        self.connection = sqlite3.connect(self.config['db_file'])
        self.cursor = self.connection.cursor()