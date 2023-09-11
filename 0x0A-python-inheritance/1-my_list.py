#!/usr/bin/python3
"""
this module defines a class that inherit from 
the list module
"""



class MyList(list):
    """
    a class that inherit from list
    """
    def print_sorted(self):
        """ a method that prints the list but sorted"""
        print(sorted(self))
