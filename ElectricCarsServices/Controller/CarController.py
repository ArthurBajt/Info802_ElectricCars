from .DataBase import db
from pymongo import ASCENDING, DESCENDING
from pymongo.database import Collection
from faker import Faker

from ..Model import Car


class CarController(object):
    collection: Collection = db["ElectricCars"]

    @classmethod #GET
    def get(cls, limit: int = None) -> dict:
        cursor = cls.collection.find({}, {'_id': False})
        if limit:
            cursor.limit(max(0, limit))
        data: list = list(cursor)
        return {"data": data,
                "size": len(data)}


    @classmethod #GET
    def find(cls, name: str) -> dict:
        cursor = cls.collection.find({"name": name}, {'_id': False}).limit(1)
        if len(list(cursor)) > 0:
            return {"data": list(cursor)[0]}
        return {}


    @classmethod #POST
    def add(cls, name: str, maker: str, year: int, range: float, price: float, charge_time: float):
        cursor = cls.collection.find({"name": name}, {'_id': False})
        if len(list(cursor)) < 1:
            car: Car = Car(name, maker, year, range, price, charge_time)
            cls.collection.insert_one(car.to_dict())


    @classmethod #PUT
    def update(cls):
        pass


    @classmethod #DELETE
    def remove(cls, name: str):
        cursor = cls.collection.find({"name": name}).limit(1)
        if cursor.get("_id"):
            cls.collection.delete_one({"_id": cursor.get("_id")})


    @classmethod
    def generate_fake(cls, amount: int = 100):
        amount = max(0, amount)
        fake: Faker = Faker()
        cls.collection.drop()
        for _ in range(0, amount):
            cls.collection.insert_one(Car.fake(fake).to_dict())
