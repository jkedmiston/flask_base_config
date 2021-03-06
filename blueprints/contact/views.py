from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for

from blueprints.contact.forms import ContactForm

contact = Blueprint("contact", __name__, template_folder="templates")


@contact.route("/contact", methods=["GET", "POST"])
def index():
    form = ContactForm()

    if form.validate_on_submit():

        flash("Thanks, expect a response shortly.", "success")
        return redirect(url_for("contact.index"))

    return render_template("contact/index.html", form=form)
