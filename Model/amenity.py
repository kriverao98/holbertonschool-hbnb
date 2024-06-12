#!/usr/bin/python3
"""This is a amenity class for the Airbnb project"""
from base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class for the airbnb project"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

    id = ""
    name = ""
