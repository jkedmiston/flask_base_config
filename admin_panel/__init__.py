from flask_admin import AdminIndexView
from flask_admin import Admin


def add_admin_app(app):
    admin = Admin(app, name="Admin", template_mode="bootstrap3", endpoint="admin",
                  index_view=AdminIndexView())
    return admin
