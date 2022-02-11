from unittest import TestCase

from ElectricCarsServices.Controller import RideController


class TestRide(TestCase):
    def test_ride_time(self):
        res: dict = RideController.ride_time(car_autonomy=25, recharge_time=10, average_speed=100, lenght=100 )
        self.assertEqual(4, res["pauses"])
        self.assertEqual(100.0, res["time"])
