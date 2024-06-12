#!/usr/bin/python3
"""This is an user class for the Airbnb project"""
from base_model import BaseModel


class User(BaseModel):
    """Defining user class attributes"""
    def __init__(self,id, email, first_name, last_name):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name


    email = ""
    password = ""
    first_name = ""
    last_name = ""
    id = ""
