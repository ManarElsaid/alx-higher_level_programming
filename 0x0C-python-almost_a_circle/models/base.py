#!/usr/bin/python3
"""A module defines Base class"""
import json
import turtle


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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        obj_list = []
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                json_string = f.read()
                list_of_dict = cls.from_json_string(json_string)
                for dict in list_of_dict:
                    obj = cls.create(**dict)
                    obj_list.append(obj)
            return obj_list
        except FileNotFoundError:
            return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ that opens a window and draws all the Rectangles and Squares"""
        zoze = turtle.Turtle()
        zoze.color("red")
        for rect in list_rectangles:
            zoze.goto(rect.x, rect.y)
            for i in range(2):
                zoze.forward(rect.height)
                zoze.left(90)
                zoze.forward(rect.width)
                zoze.left(90)

        for square in list_squares:
            zoze.goto(square.x, square.y)
            for j in range(2):
                zoze.forward(square.size)
                zoze.left(90)
                zoze.forward(square.size)
                zoze.left(90)
