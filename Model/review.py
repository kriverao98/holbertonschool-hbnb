#!/usr/bin/python3
"""A review class for the airbnb project"""
from Model.base_model import BaseModel


class Review(BaseModel):
    """A class review"""
    def __init__(self, place_id, user_id, rating, comment):
            self.place_id = place_id
            self.user_id = user_id
            self.rating = int(rating)
            self.comment = str(comment)
            super().__init__()


    
