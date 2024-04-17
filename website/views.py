# standard routes(views) of the application aside from auth
# blueprint organizes related views

from flask import Blueprint, render_template

views = Blueprint('views', __name__ )


@views.route('/')
def home():
    return render_template('home.html')