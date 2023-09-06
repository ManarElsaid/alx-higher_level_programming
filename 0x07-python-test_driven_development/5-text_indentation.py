#!/usr/bin/python3
""" prints a text with 2 new lines after each of  ., ? and :"""


def text_indentation(text):
    """
    the function prints a text with 2 lines after .,?,:

    Args:
        text(str): the text to be printed

    Returns:
        the text with 2 lines after .,?,:

    Raises:
        TypeError if the text isn't string
    """

    if (not isinstance(text, str)):
        raise TypeError("text must be a string")

    for ch in text:
        print("{}".format(ch), end="")
        if (ch == "." or ch == "?" or ch == ":"):
            print("\n")
