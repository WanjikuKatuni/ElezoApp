# standard auth routes, other routes of the application are in views

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__ )

# authentication routes

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form
    # print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) #login the user and remembers the user has logged in till the user clears their session
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password. Try again!', category='error')
        else:
            flash('Email does not exist, try again', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required # decorator that makes sure that we cannot access this route if the user has not loggedin
def logout():
    logout_user() # logout current user
    return redirect(url_for('auth.login'))



@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first() #check if user already exists
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Password should match.', category='error')
        elif len(password1) < 7:
            flash('Password should be more than 7 characters.', category='error')
        else:
            # add user
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            # add user to database session
            db.session.add(new_user)
            db.session.commit()  #commit session to db
            login_user(user, remember=True) #login the user and remembers the user has logged in till the user clears their session
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user)