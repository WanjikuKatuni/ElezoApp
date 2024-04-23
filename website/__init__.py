# initialise flask application


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager



db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ascbskfjefk fesmfawcflm' #encrypt cookie information for our data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  #show where the db is located
    db.init_app(app) #initialise database on the flask app

    

    # import the blueprint variables
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # check if db is created everytime server is run
    # import .models
    from .models import User, Note
    

    with app.app_context():
        db.create_all()


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader  #function used to load user
    def load_user(id):
        return User.query.get(int(id))




    return app

    # check if db exists and if it doesnt, it will create it and not overwirte it if it exists

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')