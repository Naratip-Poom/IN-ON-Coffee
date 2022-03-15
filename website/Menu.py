from flask import Blueprint, render_template, request, flash
from .models import User
from . import db

Menu = Blueprint('Menu', __name__)

@Menu.route('/')
def home():
    return render_template("Chose table.html")
