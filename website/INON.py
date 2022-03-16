from flask import Blueprint, render_template, request, flash, jsonify, session
from sqlalchemy import null
from .models import User
from . import db

import os
import pathlib

import requests
from flask import Flask, session, abort, redirect, request
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

app = Flask("Google Login App")
app.secret_key = "QWERTYASDFGZXCVB"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# You need to modify here
GOOGLE_CLIENT_ID = "1088598420589-ug7u23cguekm83270vtp44kk92mfhs48.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


INON = Blueprint('INON', __name__)
menu = [
    {
        "img": "../static/m1.jpg",
        "id": 1,
        "name": "Espesso",
        "price": 40,

    },

    {
    "img": "../static/m2.jpg",
    "id": 2,
        "name": "Americano",
        "price": 45,
    },

    {
    "img": "../static/m3.jpg",
    "id": 3,
        "name": "Latte",
        "price": 40,
    },

    {
    "img": "../static/m4.jpg",
    "id": 4,
        "name": "Cappucino",
        "price": 45,
    },

    {
    "img": "../static/m5.jpg",
    "id": 5,
        "name": "Mocha",
        "price": 50,
    },

    {
        "img": "../static/m6.jpg",
        "id": 6,
        "name": "Macchiato",
        "price": 40,
    },

    {
        "img": "../static/m7.jpg",
        "id": 7,
        "name": "Frappe",
        "price": 45,
    },

    {
        "img": "../static/m8.jpg",
        "id": 8,
        "name": "Affogata",
        "price": 45,
    },
]


@INON.route('/')
def home():
    return render_template("Chose table.html")

@INON.route("/logingg")
def logingg():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@INON.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    session["email"] = id_info.get("email")
    session["pic"] = id_info.get("picture")
    return redirect("/")

@INON.route('/login1', methods=['POST', 'GET']) 
def login1(): 
    return render_template("login.html")

@INON.route('/success',methods=['POST' ])
def success(): 
    if request.method == 'POST' : 
        session [ 'email'] = request.form['email']
        if  'email' in session : 
            email = session[ 'email'] 
            return render_template("profile.html", email=email)
        else : 
            return render_template("login.html") 
    return render_template("profile.html")
    


@INON.route('/final')
def final():
    return render_template("final.html", menu=menu)


@INON.route('/indexcoffee')
def index():
    return render_template("indexcoffee.html")



@INON.route('/baskettest', methods=["GET", "POST"])
def basket():
    if request.method == "POST":
        order = []
        price = 0
        for i in range(1, 9, 1):
            quantity = request.form.get(f"{i}-quantity")
            print(i, quantity)
            if quantity != "0":
                datamenu = menu[i-1]
                datamenu['topping'] = []
                
                topping2 = ''
                price += menu[i-1]["price"]

                if request.form.get(f"{i}-hot") != None:
                    # datamenu['topping'].append(request.form.get(f"{i}-hot"))
                    topping2  += (str(request.form.get(f"{i}-hot")) + ' ')
                if request.form.get(f"{i}-icde") != None:
                    # datamenu['topping'].append(request.form.get(f"{i}-iced"))
                    topping2  += (str(request.form.get(f"{i}-icde")) + ' ')
                if request.form.get(f"{i}-medium-sweet") != None:
                    # datamenu['topping'].append(request.form.get(f"{i}-medium-sweet"))
                    topping2  += (str(request.form.get(f"{i}-medium-sweet")) + ' ')
                if request.form.get(f"{i}-slightly-sweet") != None:
                    # datamenu['topping'].append(request.form.get(f"{i}-slightly-sweet"))
                    topping2  += (str(request.form.get(f"{i}-slightly-sweet")) + ' ')
                if request.form.get(f"{i}-very-sweet") != None:
                    # datamenu['topping'].append(request.form.get(f"{i}-very-sweet"))
                    topping2  += (str(request.form.get(f"{i}-very-sweet")) + ' ')

                datamenu['topping2'] = topping2 

                order.append(datamenu)
        tax = price+5

    # return request.form
    # return jsonify(order,price,tax)
        return render_template("baskettest.html", name="uuu", order=order,price=price,tax=tax)
