from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy(session_options={"autoflush": True})
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwerty asdfgh zxcvbn'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .auth import auth

    from .INON import INON

    # app.register_blueprint(auth, url_prefix='/')
    
    app.register_blueprint(INON, url_prefix='/')
    
    from .models import User,Table, Topping, Menu, Order, Item 

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
