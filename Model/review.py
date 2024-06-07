#!/usr/bin/python3
"""A review class for the airbnb project"""
from base_model import BaseModel


class Review(BaseModel):
    """A class review"""
    def __init__(self, id, text):
        def __init__(self, id, text):
            self.__id = id
            self.text = text

    id = ""
    text = ""
