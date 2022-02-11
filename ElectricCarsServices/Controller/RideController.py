class RideController(object):


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
