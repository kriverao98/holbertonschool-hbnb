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

    def rating_validation(self, rating):
        if rating < 0 or rating > 5:
            return False
        return True
    
    def review_validation(self, user_id, place_id, storage):
        if user_id not in storage['User']:
            return False
        if place_id not in storage['Place']:
             return False
        return True