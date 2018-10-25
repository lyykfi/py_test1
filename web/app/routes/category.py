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

        with connector.session_scope() as session:
            s = select([Category])
            result = session.execute(s)

            data = [{"id": x.id, "name": x.name} for x in result]
            session.close_all()

            resp.status = falcon.HTTP_200
            resp.body = json.dumps(data)