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

    def to_json(self):
        """
        a method retrieves a dictionary representation
        of a Student instance
        """
        return (self.__dict__)
