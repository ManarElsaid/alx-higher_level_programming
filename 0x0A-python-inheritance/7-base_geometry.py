#!/usr/bin/python3
"""module contains a base goemetry class"""


class BaseGeometry:
    """defines the BaseGeometry class"""
    def area(self):
        """public instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
