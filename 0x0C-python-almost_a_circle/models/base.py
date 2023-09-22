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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """a class method that writes the JSON
        string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_of_dictionary = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_of_dictionary))

    @classmethod
    def create(cls, **dictionary):
        """a method that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 5)
        else:
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy
