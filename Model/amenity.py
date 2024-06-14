#!/usr/bin/python3
"""This is a amenity class for the Airbnb project"""
from Model.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class for the airbnb project"""
    def __init__(self, name):
        self.name = name
        super().__init__()
   