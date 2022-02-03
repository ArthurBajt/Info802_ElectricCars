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
    def find(cls) -> dict:
        data: dict = {}
        return {"data": data}


    @classmethod #POST
    def add(cls):
        pass


    @classmethod #PUT
    def update(cls):
        pass


    @classmethod #DELETE
    def remove(cls):
        pass


    @classmethod
    def generate_fake(cls, amount: int = 100):
        amount = max(0, amount)
        fake: Faker = Faker()
        cls.collection.drop()
        for _ in range(0, amount):
            cls.collection.insert_one(Car.fake(fake).to_dict())
