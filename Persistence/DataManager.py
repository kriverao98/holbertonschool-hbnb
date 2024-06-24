import json
import os
from Persistence.IPersistenceManager import IPersistenceManager
from Model.base_model import BaseModel
from Model.country import Country
import pycountry


class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}

    def load_countries(self):
        countries = pycountry.countries
        for country in countries:
            country = Country(country.name, country.alpha_2)
            self.storage['Country'][country.code] = country.__dict__
        with open('countries.json', 'w') as file:
            json.dump(self.storage['Country'], file, indent=4)

    def load_all(self):
        class_names = ['Country', 'City', 'User', 'Review', 'Place', 'Amenity']
        try:
            if os.path.getsize('file_storage.json') > 0:
                with open('file_storage.json', 'r', encoding="utf-8") as file:
                    self.storage = json.load(file)
            else:
                self.storage ={}
        except FileNotFoundError:
            self.storage = {class_name: {} for class_name in class_names}
            with open('file_storage.json', 'w') as file:
                json.dump(self.storage, file, indent=4)
            self.storage = {}

    def save(self, entity):
        if not isinstance(entity, BaseModel):
            raise TypeError("entity must be an instance of BaseModel")
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        
        if entity_type == 'City':
            self.storage[entity_type][entity.id] = entity.__dict__
            if entity_type not in self.storage['Country'][entity.country_code]:
                self.storage['Country'][entity.country_code][entity_type] = {}

            self.storage['Country'][entity.country_code][entity_type][entity.id] = entity.__dict__
            with open('file_storage.json', 'w') as file:
                json.dump(self.storage, file, indent=4)
        else:
            self.storage[entity_type][entity.id] = entity.__dict__
            with open('file_storage.json', 'w') as file:
                json.dump(self.storage, file, indent=4)

    def get(self, entity_id, entity_type):
        if entity_type in self.storage:
            return self.storage[entity_type][entity_id]
        return None

    def update(self, entity):
        if not isinstance(entity, BaseModel):
            raise TypeError("entity must be an instance of BaseModel")
        entity_type = type(entity).__name__

        if entity_type == 'City':
            self.storage[entity_type][entity.id] = entity.__dict__  
            self.storage['Country'][entity.country_code][entity_type][entity.id] = entity.__dict__
            with open('file_storage.json', 'w', encoding="utf-8") as file:
                json.dump(self.storage, file, indent=4)
        else:
            if entity_type in self.storage and entity.id in self.storage[entity_type]:
                self.storage[entity_type][entity.id] = entity.__dict__
                with open('file_storage.json', 'w', encoding="utf-8") as file:
                    json.dump(self.storage, file, indent=4)
            else:
                raise ValueError("Entity not found in storage")

    def delete(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            with open('file_storage.json', 'w', encoding="utf-8") as file:
                json.dump(self.storage, file, indent=4)
        else:
            raise ValueError("Entity not found in storage")