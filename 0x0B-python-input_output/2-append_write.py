#!/usr/bin/python3
"""A module contains a function
appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as text_file:
        return (text_file.write(text))
