# standard routes(views) of the application aside from auth
# blueprint organizes related views

from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__ )


@views.route('/')
@login_required  #cannot get to home page if you have not logged in
def home():
    return render_template('home.html', user=current_user)