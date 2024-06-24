#!/usr/bin/python3
"""This is a city class for the airbnb project"""
from Model.base_model import BaseModel


class City(BaseModel):
    """A city class"""
    def __init__(self, name, country_code):
        self.name = name
        self.country_code = country_code
        super().__init__()
  

    def unique_city(self, cities_dict, name):
        for city_id, city_data in cities_dict.items():
            if city_data['name'] == name:
                return False
        return True

        