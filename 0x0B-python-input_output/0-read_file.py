#!/usr/bin/python3
"""Module containing read_file function
"""


def read_file(filename=""):
    """function that reads a text file (UTF8)
       and prints it to stdout
        Args:
            filename : the name of the file
        Returns:
            void
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()

    print(read_data, end="")
