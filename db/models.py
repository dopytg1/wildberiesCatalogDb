from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Catalog(Base):
    __tablename__ = "catalog"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    url = Column(String, default=True)
    shard = Column(String, default=True)
    query = Column(String, default=True)
    landing = Column(Boolean, default=True)

    child = relationship("Category")


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    url = Column(String, default=True)
    shard = Column(String, default=True)
    query = Column(String, default=True)
    landing = Column(String, default=True)
    parent_id = Column(Integer, ForeignKey("catalog.id"))

    child = relationship("SubCategory")


class SubCategory(Base):
    __tablename__ = "subcategory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    url = Column(String, default=True)
    shard = Column(String, default=True)
    query = Column(String, default=True)
    parent_id = Column(Integer, ForeignKey("category.id"))

    child = relationship("SubSubCategory")


class SubSubCategory(Base):
    __tablename__ = "subsubcategory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    url = Column(String, default=True)
    shard = Column(String, default=True)
    query = Column(String, default=True)
    parent_id = Column(Integer, ForeignKey("subcategory.id"))
