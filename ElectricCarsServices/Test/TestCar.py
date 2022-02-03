from unittest import TestCase

from faker import Faker

from ElectricCarsServices.Model import Car


class TestCar(TestCase):
    def test_can_create_car(self):
        car: Car = Car("test", "test maker", 2000, 999999, 240, 60)
        self.assertTrue(car != None)

    def test_can_parse_car_to_dict(self):
        car: Car = Car("test", "test maker", 2000, 999999, 240, 60)
        res: dict = car.to_dict()
        self.assertTrue(res != None and res != {})
        self.assertTrue(type(res) == dict)


    def test_can_parse_dict_to_car(self):
        data: dict = {"name": "name",
            "maker": "maker",
            "year": 2000,
            "range": 99999,
            "price": 240,
            "charge_time": 60}

        bs_data: dict = {"something false" : False}

        car: Car = Car.dict_to_instance(data)
        bs_car: Car = Car.dict_to_instance(bs_data)

        self.assertTrue(car != None)
        self.assertTrue(bs_car == None)


    def test_generate_fake_car(self):
        fake: Faker = Faker()
        car: Car = Car.fake(fake)
        self.assertTrue(car != None)
