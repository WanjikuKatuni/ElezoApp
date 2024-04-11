# standard routes(views) of the application aside from auth

from flask import Blueprint

views = Blueprint('views', __name__ )


@views.route('/')
def home():
    return "<h1>Test</h1>"