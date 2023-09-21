#!/usr/bin/python3
"""A module defines Base class"""
import json


class Base:
    """represents Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a static method returns the JSON
        string representation of list_dictionarie"""
        if (list_dictionaries is None or list_dictionaries == []):
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """a class method that writes the JSON
        string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, mode='w', encoding='utf-8') as file_name:
            if list_objs is None:
                file_name.write = "[]"
            else:
                list_of_dictionary = [obj.to_dictionary() for obj in list_objs]
                json.dump(cls.to_json_string(cls.to_json_string(list_of_dictionary)), file_name)
