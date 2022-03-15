from flask import Blueprint, render_template, request, flash
from .models import User
from . import db

INON = Blueprint('INON', __name__)
menu = [
    {
        "id": 1,
        "name": "Espesso";
        "price": 40;
        
    },

    {
    "id": 2,
        "name": "Americano";
        "price": 45;
    },

    {
    "id": 3,
        "name": "Latte";
        "price": 40;
    },

    {
    "id": 4,
        "name": "Cappucino";
        "price": 45;
    },

    {
    "id": 5,
        "name": "Mocha";
        "price": 50;
    },

    {
    "id": 6,
        "name": "Macchiato";
        "price": 40;
    },

    {
    "id": 7,
        "name": "Frappe";
        "price": 45;
    },

    {
    "id": 8,
        "name": "Affogata";
        "price": 45;
    },
]

@INON.route('/')
def home():
    return render_template("Chose table.html")

@INON.route('/final')
def final():
    return render_template("final.html",menu=menu)

@INON.route('/indexcoffee')
def index():
    return render_template("indexcoffee.html")

@INON.route('/baskettest')
def basket():
    return render_template("baskettest.html")
