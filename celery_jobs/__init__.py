from extensions import celery


@celery.task
def generic_task(arg1, arg2):
    """
    """
    print(arg1, arg2)
    return 0
