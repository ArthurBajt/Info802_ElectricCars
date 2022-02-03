import warnings
from random import randrange

from faker import Faker

from . import AbstractData


class Car(AbstractData):

    _name: str
    _maker: str
    _year: int
    _range: float
    _price: float
    _charge_time: float


    def __init__(self, name: str, maker: str, year: int, range: float, price: float, charge_time: float):
        super(Car, self).__init__()
        self._name = name
        self._maker = maker
        self._year = year
        self._range = range
        self._price = price
        self._charge_time = charge_time


    def to_dict(self) -> dict:
        return {
            "name": self._name,
            "maker": self._maker,
            "year": self._year,
            "range": self._range,
            "price": self._price,
            "charge_time": self._charge_time
        }


    @classmethod
    def dict_to_instance(cls, data: dict):
        required_keys: list[str] = ["name", "maker", "year", "range", "price", "charge_time"]
        has_required_keys: bool = True
        for key in required_keys:
            has_required_keys = has_required_keys and (key in data.keys())

        if has_required_keys:
            return Car(
                name=str(data["name"]),
                maker=str(data["maker"]),
                year=int(data["year"]),
                range=float(data["range"]),
                price=float(data["price"]),
                charge_time=float(data["charge_time"])
            )

        warnings.warn("Could not parse the given data to a Car instance")
        return None


    @classmethod
    def fake(cls, faker: Faker):
        return Car(
            name=faker.first_name() + " " + faker.bs(),
            maker=faker.company(),
            year=randrange(2016, 2022),
            range=randrange(100, 1200, 5),
            price=randrange(7000, 100000, 100),
            charge_time=randrange(30, 480)
        )
