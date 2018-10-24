from sqlalchemy import Column, Integer, String, UniqueConstraint

from web.db.connect import Base


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
