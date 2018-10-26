from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from web.db.connect import Base

class CategoryAssociation(Base):
    __tablename__ = 'category_association'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('category.id'))
    child_id = Column(String, ForeignKey('category.id'))

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    children = relationship(
        "Category",
        secondary=CategoryAssociation.__table__,
        primaryjoin=CategoryAssociation.__table__.c.parent_id == id,
        secondaryjoin=CategoryAssociation.__table__.c.child_id == id,
    )
    parent = relationship(
        "Category",
        secondary=CategoryAssociation.__table__,
        primaryjoin=CategoryAssociation.__table__.c.child_id == id,
        secondaryjoin=CategoryAssociation.__table__.c.parent_id == id,
    )
