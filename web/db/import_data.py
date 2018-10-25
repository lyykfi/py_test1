""" """
from sqlalchemy.exc import IntegrityError

from web.db.models.category import Category, CategoryAssociation
from .connect import DBConnector

class DBImport:
    def __init__(self):
        # init connector
        self.connector = DBConnector()

    def _check_category_exist(self, session, name):
        q = session.query(Category).filter(Category.name == name).exists()
        return session.query(q).scalar()

    def _add_category(self, session, category, parent = None):
        name = category["name"]

        if self._check_category_exist(session, name) == False:
            newCategory = Category(name=name)

            session.add(newCategory)
            session.flush()

            if parent:
                categoryAssociate = CategoryAssociation(parent_id=parent.id, child_id=newCategory.id)
                session.add(categoryAssociate)

            for sub_category in category.get("items") or []:
                self._add_category(session, sub_category, newCategory)

    def import_data(self, data):
        with self.connector.session_scope() as session:
            for category in data["categories"]:
                try:
                    self._add_category(session, category)
                except IntegrityError:
                    pass




