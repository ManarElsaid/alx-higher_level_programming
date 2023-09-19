#!/usr/bin/python3
""" Defines a class rectangle"""


class Rectangle:
    """represents a class rectangle"""
    def __init__(self, width=0, height=0):
        """initialization of the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """reteives the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set rectangle width"""
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get rectangle height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set rectangle height"""
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public method returns a rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns a rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
