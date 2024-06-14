#!/usr/bin/python3
"""This is a city class for the airbnb project"""
from Model.base_model import BaseModel


class City(BaseModel):
    """A city class"""
    def __init__(self, name, country_code):
        self.name = name
        self.country_code = country_code
        super().__init__()
  
