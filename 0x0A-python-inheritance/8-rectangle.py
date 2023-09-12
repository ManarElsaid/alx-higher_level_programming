#!/usr/bin/python3
""" a subclass from base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle which inherit from BaseGeometry"""
    def __init__(self, width, height):
        """initialize a new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
