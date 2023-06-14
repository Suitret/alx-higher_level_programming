#!/usr/bin/python3
"""Module containing append_write function
"""


def append_write(filename="", text=""):
    """function that appends a string to a text
       file (UTF8) and returns the number of
       characters written
        Args:
            filename : the name of the file
            text : string to add
        Returns:
            number of char written
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        nb_char = f.write(text)

    return nb_char
