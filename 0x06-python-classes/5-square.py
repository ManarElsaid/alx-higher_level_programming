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

    @property
    def size(self):
        """retrieves the square size"""
        return (self.__size)

    @setter
    def size(self, value):
        """setter for size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """defines the area of the square"""

        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if (size == 0):
            print()

        for i in range(self.__size):
            print("#" * self.__size)
