from requests import get, post, Response
from ElectricCarsServices.Controller.CarController import CarController


class RideController(object):

    URL_POINT_TO_POINT: str = "http://router.project-osrm.org/route/v1/driving/{},{};{},{}"

    @classmethod
    def ride_time(cls, car_autonomy: float, recharge_time: float, average_speed: float, lenght: float) -> dict:
        """
        Calculate how long a ride will be in minutes
        :param car_autonomy: car autonomy in kilometer
        :param recharge_time: how long is the recharge time in minutes
        :param average_speed: the average speed in km/h
        :param lenght: the lenght of the ride in km
        :return: how many pauses you will take to recharge your car, and how long the journey will last en minutes
        """
        if car_autonomy == 0.0 or average_speed == 0.0:
            return {}

        pauses: int = int(lenght / car_autonomy)
        road_time: float = (lenght / average_speed) * 60
        res: dict = {
            "time": recharge_time * pauses + road_time,
            "pauses": pauses
        }
        return res


    @classmethod
    def distance_between_point(cls, from_latitude: float, from_longitude: float, to_latitude: float, to_longitude: float) -> float:
        """
        Gives the shortest road distance between 2 point
        :param a: the cordinates from where you start
        :param b: the cordinates of where you are going
        :return: the road distance in kilometer between two point, -1.0 if there not route possible
        """
        res: Response = get(cls.URL_POINT_TO_POINT.format(from_latitude, from_longitude, to_latitude, to_longitude))
        if res.status_code == 200:
            res_json: dict = res.json()
            if res_json["code"] == "Ok":
                if len(res_json["routes"]) > 0:
                    return float(res_json["routes"][0]["legs"][0]["distance"] / 1000.0)
        return -1.0


    @classmethod
    def car_ride(cls, car_name: str, from_latitude: float, from_longitude: float, to_latitude: float, to_longitude: float):
        car: dict = CarController.find(car_name)['data']
        print(car)

        if car == {}:
            return {"error": "no car found"}

        distance: float = cls.distance_between_point(from_latitude, from_longitude, to_latitude, to_longitude)
        if distance < 0.0:
            return {"error": "can t go from A to B with a car"}

        res: dict = cls.ride_time(car['range'], car['charge_time'], 100.0, distance)
        return {"data": {"ride": res,
                         "car": car,
                         "speed": 100.0}}
