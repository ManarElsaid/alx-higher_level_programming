#!/usr/bin/python3
"""defines the class rectangle inherits
from Base class"""
from models.base import Base


class Rectangle(Base):
    """represents subclass Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):

        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        
        if (not isinstance(height, int)):
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")

        if (not isinstance(x, int)):
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")

        if (not isinstance(y, int)):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__x = y

        super().__init__(id)

    def set_width(self):
        self.__width = width

    def get_width(self):
        return (self.__width)

    def set_height(self):
        self.__height = height

    def get_height(self):
        return (self.__height)

    def set_x(self):
        self.__x = x

    def get_x(self):
        return (self.__x)

    def set_y(self):
        self.__y = y

    def get_y(self):
        return (self.__y)
