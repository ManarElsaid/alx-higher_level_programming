#!/usr/bin/python3
"""Module to write a string to a text file """


def write_file(filename="", text=""):
    """
    this function a function that writes a string to a text file
    (UTF8) and returns the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as text_file:
        return (text_file.write(text))
