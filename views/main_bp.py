from flask import Blueprint, render_template


main_bp = Blueprint(
    'main_bp',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/', methods=["GET"])
def index():
    print("hello from index")
    return "hi"
