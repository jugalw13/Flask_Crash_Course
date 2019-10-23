from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # The app.config is a dictionary object which can be
    # edited. It can be used to assign values to some 
    # built-in configurations or to setup your own 
    # configurations for flask extensions.

    # Disable unncessary update trackings
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # Make sure to create a db named todo in phpmyadmin
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/todo'
    db.init_app(app)

    from .models import TODO    

    # The app.app_context() method keeps track of the current flask
    # application. We use it here to make sure that db.create_all()
    # adn routes are called whenever a new flask app is created
    with app.app_context():
        db.create_all()
        from . import routes

    return app 
