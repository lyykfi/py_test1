""" Category server resource """
import json

import falcon
from sqlalchemy.orm import lazyload

from web.db.connect import DBConnector
from web.db.models.category import Category


class CategoryResource(object):
    def _get_category_dic(self, category):
        new_category = {
            "id": category.id,
            "name": category.name,
            "children": [self._get_category_dic(x) for x in category.children]
        }

        return new_category

    def on_get(self, req, resp):
        # init connector
        connector = DBConnector()

        with connector.session_scope() as session:
            result = session.query(Category).options(lazyload(Category.children)).filter_by(parent=None).all()

            data = [self._get_category_dic(x) for x in result]

            resp.status = falcon.HTTP_200
            resp.body = json.dumps(data)