from flask import Blueprint, render_template, url_for

from ElectricCarsServices.Controller import CarController

app: Blueprint = Blueprint('home', __name__, url_prefix='/')


@app.route('/')
@app.route('/home')
def home():
    data: dict = {"cars": CarController.get()}
    return render_template("index.html", data=data)


@app.route('/test_services')
def test_services():
    services: list[dict] = [
        {"name": "Ride Time", "url": url_for("Ride.time")}
    ]

    data: dict = {"cars": CarController.get(),
                  "services": services}

    return render_template("test_services.html", data=data)
