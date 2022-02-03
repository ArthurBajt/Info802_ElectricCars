from unittest import TestCase

from ElectricCarsServices.Controller import RideController


class TestRide(TestCase):
    def test_ride_time(self):
        res: dict = RideController.ride_time(10, 10, 100, 10000)
        self.assertEqual({"pauses": 1000, "time": 10100.0}, res)
