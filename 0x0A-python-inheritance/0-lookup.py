#!/usr/bin/python3
"""
this module returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    this method returns the a vailable attributes and methods
    of an object obj and returns a list of them
    """
    return (dir(obj))
