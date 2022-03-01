from flask import Blueprint, request

from ElectricCarsServices.Controller import RideController


app: Blueprint = Blueprint("Ride", __name__, url_prefix="/ride")


@app.route('/time', methods=['POST'])
def time():
    length: float = float(request.form.get("length"))
    car_autonomy: float = float(request.form.get("car_autonomy"))
    car_charge_time: float = float(request.form.get("car_charge_time"))
    car_average_speed: float = float(request.form.get("car_average_speed"))
    return RideController.ride_time(car_autonomy, car_charge_time, car_average_speed, length)


@app.route('/distance', methods=['POST'])
def distance():
    from_latitude: float = float(request.form.get("from_latitude"))
    from_longitude: float = float(request.form.get("from_longitude"))
    to_latitude: float = float(request.form.get("to_latitude"))
    to_longitude: float = float(request.form.get("to_longitude"))
    return {"distance": RideController.distance_between_point(from_latitude, from_longitude, to_latitude, to_longitude)}


@app.route('/car_ride', methods=['GET', 'POST'])
def car_ride():
    from_latitude: float = float(request.form.get("from_latitude"))
    from_longitude: float = float(request.form.get("from_longitude"))
    to_latitude: float = float(request.form.get("to_latitude"))
    to_longitude: float = float(request.form.get("to_longitude"))
    car_name: str = str(request.form.get("car_name"))

    return RideController.car_ride(car_name, from_latitude, from_longitude, to_latitude, to_longitude)
