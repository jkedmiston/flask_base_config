# Overview
Basic template for python projects. 
Includes
* precommit configuration
* alembic configuration w/SQLAlchemy

# Precommit
An excellent tool for automatic code checks. 
* ref for pylint: https://moserei.de/2020/10/28/pylint-pre-commit-hook.html

# Flask-Migrate
* from blank container, `flask db init` generates env.py, alembic.ini
* `flask db migrate -m initial migrate`
* `flask db upgrade`

# First usage
* `cp env.sample .env`
* `docker-compose build`
* `docker-compose run --rm webapp flask db upgrade`
* `docker-compose up`

