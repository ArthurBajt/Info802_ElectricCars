from flask import Blueprint

from .HomeServices import app as bp_home
from .CarServices import app as bp_cars


services: list[Blueprint] = [
    bp_home,
    bp_cars
]
