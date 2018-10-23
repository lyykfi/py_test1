import json

from package.db.connect import DBConnector
from package.db.sql import DBSQL
from package.db.tables import DBTables

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/category")
def get_category():
    # init connector
    connector = DBConnector()
    # init db sql
    db_sql = DBSQL()

    sql_select = db_sql.get_sql_from_file(DBTables.CATEGORY.value, 'select')
    
    cursor = connector.connection.cursor()
    result = cursor.execute(sql_select)
    data = cursor.fetchall()
    cursor.close()

    print(data)

    return json.dumps(data)