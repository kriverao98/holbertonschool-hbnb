#!/usr/bin/python3
"""class Place for Airbnb project"""
from Model.base_model import BaseModel


class Place(BaseModel):
    """Place class for Airbnb project"""
    def __init__(self, host_id, city_id, amenity_id,  name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude):
        self.host_id = host_id
        self.city_id = city_id
        self.amenity_id = amenity_id
        self.name = str(name)
        self.description = str(description)
        self.number_rooms = int(number_rooms)
        self.number_bathrooms = int(number_bathrooms)
        self.max_guest = int(max_guest)
        self.price_by_night = float(price_by_night)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        super().__init__()
