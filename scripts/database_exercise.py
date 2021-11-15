"""
Exercise some models on the production database.
"""
import os

import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy.orm import Session

from database.schema import User

load_dotenv(".env")

engine = sqlalchemy.create_engine(os.environ["DB_URL"])
with Session(engine) as session:
    some_object = User(name="Ted")
    session.add(some_object)
    session.commit()
    id_to_delete = some_object.id

session = Session(engine)
us = session.query(User).all()
for u in us:
    print(u)


us = session.query(User).filter(User.name == "Ted").all()
for u in us:
    session.delete(u)

session.commit()
