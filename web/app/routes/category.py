""" Category server resource """
import json

import falcon
from sqlalchemy import select

from web.db.connect import DBConnector
from web.db.models.category import Category


class CategoryResource(object):
    def on_get(self, req, resp):
        # init connector
        connector = DBConnector()

        s = select([Category])
        result = connector.session.execute(s)

        data = list(map(lambda x: x.name, result))

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(data)