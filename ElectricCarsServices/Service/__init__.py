from flask import Blueprint

from .HomeServices import app as bp_home
from .CarServices import app as bp_cars
from .RideService import app as bp_ride
from .TestServices import app as bp_test_services


services: list[Blueprint] = [
    bp_home,
    bp_cars,
    bp_ride,
    bp_test_services
]
