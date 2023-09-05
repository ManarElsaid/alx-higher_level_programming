#!/usr/bin/python3
""" prints a square with charachter #"""


def print_square(size):
    """
    the function prints a square with charachter #

    Args:
        size(int): the size of the square

    Returns:
        printed square with #

    Raises:
        TypeError if the size isn't integer or the size is float 
        and less than zero
        ValueError if size is less than zero
    """

    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")

    if (size < 0):
        raise ValueError("size must be >= 0")

    if (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    for row in range(size):
        for colomn in range(size):
            print("#", end="")
        print()
