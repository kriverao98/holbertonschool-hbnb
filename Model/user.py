#!/usr/bin/python3
"""This is an user class for the Airbnb project"""

class User:
    """Defining user class attributes"""
    def __init__(self, email, password, first_name, last_name, id):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    id = ""
