from flask import Blueprint, render_template, url_for

from ElectricCarsServices.Controller import CarController

app: Blueprint = Blueprint('Test', __name__, url_prefix='/test')


@app.route('/')
def testes():
    links: list = [
        url_for("Test.time"),
        url_for("Test.distance"),
        url_for("Test.car_ride")
    ]
    return render_template("test_list.html", data={"links": links})


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


@app.route('/car_ride')
def car_ride():
    cars: list = CarController.get()['data']
    cars = sorted(cars, key=lambda a: a['range'], reverse=False)
    data: dict = {"cars": cars}

    return render_template("test_car_ride.html", data=data)
