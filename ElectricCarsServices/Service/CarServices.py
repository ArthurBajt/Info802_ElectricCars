import json

from flask import Blueprint

from ElectricCarsServices.Controller import CarController

app: Blueprint = Blueprint("Cars", __name__, url_prefix="/cars")


@app.route('/')
def index_cars():
    return CarController.get()


@app.route('/generate')
def generate():
    CarController.generate_fake()
    return "OK"


