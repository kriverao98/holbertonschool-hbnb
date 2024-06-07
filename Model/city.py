#!/usr/bin/python3
"""This is a city class for the airbnb project"""
from base_model import BaseModel


class City(BaseModel):
    """A city class"""
    def __init__(self, id, name):
        self.__id = id
        self.name = name

    id = ""
    name = ""
