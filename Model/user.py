#!/usr/bin/python3
"""This is an user class for the Airbnb project"""
from Model.base_model import BaseModel
from datetime import datetime


class User(BaseModel):
    """Defining user class attributes"""
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        super().__init__()
    
    def unique_user(self, users_dict, email):
        for user_id, user_data in users_dict.items():
            if user_data['email'] == email:
                return False
        return True
