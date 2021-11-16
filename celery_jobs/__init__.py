from extensions import celery


@celery.task
def generic_task(arg1, arg2):
    """Basically something to test celery workers environment"""
    print(arg1, arg2)
    return 0
