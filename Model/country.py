#!/usr/bin/python3
"""A country class for the Airbnb project"""
from base_model import BaseModel


class Country(BaseModel):
    """A country class"""
    def __init__(self, name):
        self.name = name

    name = ""
