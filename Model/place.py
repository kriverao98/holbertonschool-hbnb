#!/usr/bin/python3
"""class Place for Airbnb project"""

class Place:
    """Place class for Airbnb project"""
    def __init__(self, id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude):
        self.id = id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self. number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude

    id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0.0
    latitude = 0.0
    longitude = 0.0
