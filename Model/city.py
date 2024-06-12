#!/usr/bin/python3
"""This is a city class for the airbnb project"""
from base_model import BaseModel


class City(BaseModel):
    """A city class"""
    def __init__(self, id, name, country_code):
        self.id = id
        self.name = name
        self.country_code = country_code

    id = ""
    name = ""
