#!/usr/bin/python3
"""Base model class that other classes inherit from"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base model class that other classes inherit from"""
    
    def __init__(self, id = None, created_at = None, updated_at = None):
        """Initilises BaseModel instance"""
        self.id = id if id else str(uuid4())
        self.created_at = str(created_at if created_at else datetime.now())
        self.update_at = created_at
        if created_at != updated_at:
            self.update_at = str(datetime.now())

    def update(self):
        self.update_at = str(datetime.now())
