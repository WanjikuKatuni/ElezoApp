# standard auth routes, other routes of the application are in views

from flask import Blueprint, render_template

auth = Blueprint('auth', __name__ )

# authentication routes

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')