#!/usr/bin/python3
""" this module check if an object is exactly
an instance of a specified class"""


def is_same_class(obj, a_class):
    """
    Defines a method that returns True if the object is
    exactly an instance of the specified class otherwise False
    """
    return (isinstance(obj, a_class))
