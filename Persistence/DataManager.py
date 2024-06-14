import json
import os
from Persistence.IPersistenceManager import IPersistenceManager
from Model.base_model import BaseModel
from Model.country import Country


class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {}

    def load_countries(self):
        try:
            with open('countries.json', 'r') as f:
                countries = json.load(f)
        except FileNotFoundError:
            self.storage['Country'] = {}
            return
        except json.JSONDecodeError:
            print("Error decoding JSON file")
            self.storage['Country'] = {}
            return

        self.storage['Country'] = {}
        for country in countries:
            try:
                country_code = country['country_code']
                self.storage['Country'][country_code] = country
            except KeyError:
                print(f"KeyError: One of the countries does not have a 'country_code' key")

    def load_all(self):
        try:
            if os.path.getsize('file_storage.json') > 0:
                with open('file_storage.json', 'r', encoding="utf-8") as file:
                    self.storage = json.load(file)
            else:
                self.storage ={}
        except FileNotFoundError:
            self.storage = {}

    def save(self, entity):
        if not isinstance(entity, BaseModel):
            raise TypeError("entity must be an instance of BaseModel")
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
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
                json.dump(self.storage, file)
        else:
            raise ValueError("Entity not found in storage")