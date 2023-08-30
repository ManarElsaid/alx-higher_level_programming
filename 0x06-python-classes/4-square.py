#!/usr/bin/python3
"""Defines a square"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """intialization the square with size

        Arg:
           size (int): the size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size(self):
        """getter to retreive the data

        Arg:
           size(int): the size of the square"""
        return self.__size

    def size(self, value):
        """setter to set the data

        Arg:
           size(int): the size of the data"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """defines the area of the square"""

        return (self.__size * self.__size)
