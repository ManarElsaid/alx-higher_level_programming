#!/usr/bin/python3

def add_integer(a, b=98):
    """
    this function adds two integers and return the output

    Args:
        a(int): the first integer
        b(int): the second integer

    Returns:
        int: the sum of the 2 integers

    Raises:
        TypeError if a or b is not integer of float
    """

    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
