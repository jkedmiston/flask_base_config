from flask import Blueprint

from celery_jobs import generic_task

main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)


@main_bp.route("/", methods=["GET"])
def index():
    print("hello from index")
    generic_task.delay(1, 2)
    return "hi"
