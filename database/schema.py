"""
Basic SQLAlchemy models as a placeholder
"""
# pylint: disable=too-few-public-methods
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """
    A placeholder db model
    """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<User: {self.name}"


class Plant(Base):
    """
    A placeholder db model
    """

    __tablename__ = "plant"
    id = Column(Integer, primary_key=True)
    name = Column(String)
