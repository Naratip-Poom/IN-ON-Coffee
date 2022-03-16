from flask import Blueprint, render_template, request, flash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template("home.html")

@auth.route('/login', methods=['POST', 'GET']) 
def login(): 
    return render_template("login.html")
    
@auth.route('/login1', methods=['POST', 'GET']) 
def login1(): 
    return redirect(url_for("auth.login"))


@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')

    return render_template("signup.html")
