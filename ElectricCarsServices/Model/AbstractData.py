from abc import ABC, abstractmethod

from faker import Faker


class AbstractData(ABC):

    @abstractmethod
    def to_dict(self) -> dict:
        """ Parse the instance to a dictionnary """
        return {}

    @staticmethod
    @classmethod
    @abstractmethod
    def dict_to_instance(cls, data: dict):
        """
        Create an instance of the class from the data of a dictionary
        :param data: the dictionary
        :return: an instance of the class
        """
        return None


    @classmethod
    @abstractmethod
    def fake(cls, faker: Faker):
        """
        Generate a fake instance of the class
        :param faker: The faker used to generate an instance
        :return: a fake instance of the class
        """
        return None
