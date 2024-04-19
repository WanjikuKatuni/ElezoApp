# initialise flask application


from flask import Flask
from flask_sqlalchemy import SQLAlchemy



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

    return app