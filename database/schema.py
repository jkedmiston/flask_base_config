"""
Basic SQLAlchemy models as a placeholder
"""
# pylint: disable=too-few-public-methods
from extensions import db


class User(db.Model):
    """
    A placeholder db model
    """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f"<User: {self.name}"


class Plant(db.Model):
    """
    A placeholder db model
    """

    __tablename__ = "plant"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
