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

    def area(self):
        """defines the area of the square"""

        return (self.__size * self.__size)
