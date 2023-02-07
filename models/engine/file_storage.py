#!/usr/bin/python3
"""This module defines a class ``FileStorage`` that
serializes instances to a JSON file and deserializes a JSON file to instances
"""

import json
import os


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances

    Attributes:
        file_path (str): the path to the JSON file
        __objects (dictionary): empty but will store all objects
        by <class name>.id
        (ex: to store a BaseModel object with id=12121212,
        the key will be BaseModel.12121212)
    """

    __file_path = os.path.join(os.getcwd(), "file_storage.json")
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            obj (BaseModel): a ``BaseModel`` instance
        """

        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        dict_repr = {}
        for key, value in FileStorage.__objects.items():
            dict_repr[key] = value.to_dict()
        with open(FileStorage.__file_path, 'a', encoding='utf-8') as f:
            json.dump(dict_repr, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists otherwise, does nothing"""

        FileStorage.__objects = {}
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as f:
            return json.load(f)
