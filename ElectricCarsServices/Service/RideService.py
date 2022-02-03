from flask import Blueprint, request

from ElectricCarsServices.Controller import RideController


app: Blueprint = Blueprint("Ride", __name__, url_prefix="/ride")


@app.route('/time', methods=['POST'])
def time():
    length: float = float(request.form.get("length"))
    car_autonomy: float = float(request.form.get("car_autonomy"))
    car_charge_time: float = float(request.form.get("car_charge_time"))
    return RideController.ride_time(car_autonomy, car_charge_time, 50.0, length)
