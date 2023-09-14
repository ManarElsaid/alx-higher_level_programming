#!/usr/bin/python3
"""
a module contains class studen
"""


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
        attr = self.__dict__
        if (isinstance(attrs, str)):
            for atr in attrs:
                return (attr[atr])
        return (attrs)
