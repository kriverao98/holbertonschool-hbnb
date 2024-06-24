#!/usr/bin/python3
"""A country class for the Airbnb project"""
from Model.base_model import BaseModel
import pycountry #type: ignore


class Country(BaseModel):
    """A country class"""
    def __init__(self, name, code):
        self.name = str(name)
        self.code = code

    
    def get_code(self):
        """Method for obtaining alpha-2 code for Country class

        Args:
            code (alpha-2): Variable that gets alpha-2 code

        Returns:
            None
        """
        try:
            code = pycountry.countries.lookup(code)
            return code.alpha_2
        except LookupError:
            return None
