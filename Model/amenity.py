#!/usr/bin/python3
"""This is a amenity class for the Airbnb project"""
from Model.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class for the airbnb project"""
    def __init__(self, name):
        self.name = name
        super().__init__()
   
    def unique_amenity(self, amenities_dict, name):
        for amenity_id, amenity_data in amenities_dict.items():
            if amenity_data['name'] == name:
                return False
        return True