from flask import Blueprint, render_template, url_for

from ElectricCarsServices.Controller import CarController

app: Blueprint = Blueprint('Test', __name__, url_prefix='/test')


@app.route('/time')
def time():
    services: list[dict] = [
        {"name": "Ride Time", "url": url_for("Ride.time")}
    ]

    data: dict = {"cars": CarController.get(),
                  "services": services}

    return render_template("test_time.html", data=data)


@app.route('/distance')
def distance():
    data: dict = {"cars": CarController.get()}

    return render_template("test_distance.html", data=data)