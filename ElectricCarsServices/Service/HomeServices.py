from flask import Blueprint, render_template, url_for

from ElectricCarsServices.Controller import CarController

app: Blueprint = Blueprint('home', __name__, url_prefix='/')


@app.route('/')
@app.route('/home')
def home():
    data: dict = {"cars": CarController.get()}
    return render_template("index.html", data=data)


@app.route('/help')
def help():
    return render_template("help.html")


@app.route('/map')
def map():
    return render_template("map.html")

