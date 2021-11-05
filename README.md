# Overview
Basic template for python projects. 

# Precommit
An excellent tool for automatic code checks. 
* ref for pylint: https://moserei.de/2020/10/28/pylint-pre-commit-hook.html

# Alembic setup
For autogenerating migrations, with SQLite and schema at `database/schema.py`. 
* `pip install alembic`
* `alembic init alembic`
* Edit alembic ini to point `sqlalchemy.url` to the database location, e.g. `sqlite:///db.db`
* Edit `alembic/env.py` to point at 
```
from schema import Base  # noqa
target_metadata = Base.metadata
```
* Starting with blank schema, `alembic revision -m "init"` followed by `alembic upgrade head` will initialize the database (db.db). 
* Changes to `database/schema.py` are then registered with `alembic revision --autogenerate -m "rev name"` and `alembic upgrade head`. 

