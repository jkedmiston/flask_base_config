"""
Set up celery beat worker
"""
# pylint: disable=wrong-import-position, unused-wildcard-import
from datetime import timedelta

from extensions import celery
from main import create_app

# https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#beat-entries
celery.conf.beat_schedule = {
    "start-work": {"task": "tasks.update_number", "schedule": timedelta(seconds=10)}
}

celery.conf.timezone = "UTC"
flask_app = create_app()
celery.conf.update(flask_app.config)
flask_app.app_context().push()
from extensions import db  # noqa


@celery.task
def update_number():
    """
    Updates/adds a random number to a database
    This demonstrates database is accessible on the workers.
    """
    import numpy as np
    from database.schema import RandomData

    rd = RandomData.query.get(1)
    if rd is None:
        rd = RandomData(value=np.random.random())
        db.session.add(rd)
    else:
        rd.value = np.random.random()
    db.session.commit()
    return 0


from celery_jobs import *  # noqa # pylint: disable=wildcard-import
