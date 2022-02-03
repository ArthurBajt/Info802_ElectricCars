from flask import Blueprint, render_template

from ElectricCarsServices.Controller import CarController

app: Blueprint = Blueprint('home', __name__, url_prefix='/')


@app.route('/')
@app.route('/home')
def home():
    data: dict = {"cars": CarController.get()}
    return render_template("index.html", data=data)
