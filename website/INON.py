from flask import Blueprint, render_template, request, flash, jsonify
from sqlalchemy import null
from .models import User
from . import db


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
