#!/usr/bin/python3
"""Inside the file_storage module."""
import json
from models.base_model import BaseModel

class FileStorage:
    """Inside the FileStorage class.

    Attrs:
        __file_path (str): Path to json file.
        __objects (dict): Dict to store objs.
    """

    __file_path = 'file.json'
    __objects = {}
    
    @classmethod
    def all(cls):
        """Returns __objects"""
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        name = obj.__class__.__name__
        cls.__objects["{}.{}".format(name, obj.id)] = obj

    @classmethod
    def save(cls):
        """erializes __objects to the JSON file (path: __file_path)"""
        my_dict = cls.__objects
        new_dict = {key: my_dict[key].to_dict() for key in my_dict]
        with open(cls.__file_path, "w") as file:
            json.dump(new_dict, file)

    @classmethod
    def reload(cls):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists."""
        try:
            with open(cls.__file_path) as file:
                my_dict = json.load(file)
                for v in my_dict.values():
                    name_cls = v['__class__']
                    del v['__class__']
                    cls.new(eval(name_cls)(**v))
        except FileNotFounderror:
            return
