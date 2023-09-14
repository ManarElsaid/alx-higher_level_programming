#!/usr/bin/python3
"""
a module contains class studen
"""
import json


class Student:
    """defines a student class"""
    def __init__(self, first_name, last_name, age):
        """initialize the object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        a method retrieves a dictionary representation
        of a Student instance
        """
        attrs = self.__dict__
        if (isinstance(attrs, str)):
            return (json.dumps(attrs, sort_keys=True))
        return (json.dumps(attrs))
