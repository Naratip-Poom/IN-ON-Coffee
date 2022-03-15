from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    __tablename__ = "user"
    # Need to Set Primary Key (Unique)
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    order = db.relationship("Order")

    
class Table(db.Model):
    __tablename__ = "table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    order = db.relationship("Order")

class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    table_id = db.Column(db.Integer, db.ForeignKey("table.id"))

class Item(db.Model):
    __tablename__ = "item"
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer,db.ForeignKey("menu.id"))
    topping_id = db.Column(db.Integer,db.ForeignKey("Topping.id"))

class Topping(db.Model):
    __tablename__ = "topping"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    item = db.relationship("item")
    
class Menu(db.Model):
    __tablename__ = "menu"
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.Integer)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    item = db.relationship("item")
