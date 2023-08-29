#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """intialization the square

        Arg:
           size (int): the size of square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
