from persistence_manager import IPersistenceManager
import json


class DataManager(IPersistenceManager):
    def save(self, entity):
        with open('file_storage.json', "w", encoding="utf-8") as file:
            file.write(json.dumps(entity))

    def get(self, entity_id, entity_type):
        if isinstance(entity_id, entity_type):
            with open("file_storage.json", "r", encoding="utf-8"):
                return json.loads(entity_id)

    def update(self, entity):
        with open('file_storage.json', 'w', encoding="utf-8") as file:
            data = json.loads(file)
            data.update(entity)
            json.dumps(data)


    def delete(self, entity_id, entity_type):
        with open("file_storage.json", "r", encoding="utf-8") as file:
            data = json.loads(file)

        del data[entity_type][entity_id]

        with open("file_storage.json", "w", encoding="utf-8") as file:
            json.dump(data, file)
