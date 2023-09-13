#!/usr/bin/python3
"""a module contains a function that reads a text file"""


def read_file(filename=""):
    """
    defines a  function that reads a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, mode='r', encoding='utf-8') as text_file:
        print(text_file.read())
