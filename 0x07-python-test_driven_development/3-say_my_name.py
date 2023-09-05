#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    this function prints My name is <first name> <last name>

    Args:
        first_name(str): the first name
        last_name(str): the last name

    Returns:
        str: My name is <first name> <last name>

    Raises:
        TypeError if one of the two args not string
    """
    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")

    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
