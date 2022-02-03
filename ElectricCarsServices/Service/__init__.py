from flask import Blueprint

from .HomeServices import app as bp_home
from .CarServices import app as bp_cars
from .RideService import app as bp_ride


services: list[Blueprint] = [
    bp_home,
    bp_cars,
    bp_ride
]
