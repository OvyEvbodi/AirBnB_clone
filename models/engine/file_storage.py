#!/usr/bin/python3
"""This module defines a class ``FileStorage`` that
serializes instances to a JSON file and deserializes a JSON file to instances
"""

import json
import os


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = os.path.join(os.getcwd(), "file_storage.json")
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets a new object

        Args:
            obj (BaseModel): a ``BaseModel`` instance
        """

        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes an objects to the JSON file"""

        dict_repr = {}
        for key, value in FileStorage.__objects.items():
            dict_repr[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dict_repr, f)

    def reload(self):
        """Deserializes the JSON file to dictionary of objects if file exists
        """

        from models.base_model import BaseModel
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.user import User

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        filename = FileStorage.__file_path

        try:
            with open(filename, "r") as file:
                data = json.load(file)
                FileStorage.__objects = {key: classes[value["__class__"]](
                    **value) for key, value in data.items()}
        except FileNotFoundError:
            pass
