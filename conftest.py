# pylint: disable=redefined-outer-name, protected-access, unused-argument
import os
import sys
import tempfile

import pytest

from config import Config

Config.TESTING = True


@pytest.fixture
def app(monkeypatch):
    """
    Todo: make postgres version
    - https://blog.jetbridge.com/python-2020-modern-best-practices/
    - https://pypi.org/project/pytest-postgresql/
    """
    from main import create_app
    from extensions import db

    db_fd, database = tempfile.mkstemp()
    database_url = "sqlite:///%s" % database
    os.environ["DATABASE_URL"] = database_url
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
    monkeypatch.setattr(Config, "SQLALCHEMY_DATABASE_URI", database_url)
    app = create_app()  # calls register_extensions
    with app.app_context():
        db.create_all()
        yield app
    # See https://flask.palletsprojects.com/en/1.1.x/testing/
    os.close(db_fd)
    os.unlink(database)


def pytest_configure(config):
    # see https://docs.pytest.org/_/downloads/en/3.0.1/pdf/
    # detect if running from pytest
    sys._called_from_test = True


def pytest_unconfigure(config):
    del sys._called_from_test
