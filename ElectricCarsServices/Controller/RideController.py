class RideController(object):


    @classmethod
    def ride_time(cls, car_autonomy: float, recharge_time: float, average_speed: float, lenght: float) -> dict:
        pauses: int = int(lenght / car_autonomy)
        road_time: float = lenght / average_speed
        res: dict = {
            "time": recharge_time * pauses + road_time,
            "pauses": pauses
        }
        return res
