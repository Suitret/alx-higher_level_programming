#!/usr/bin/python3
"""Module containing save_to_json_file function
"""


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
       using a JSON representation
        Args:
            my_obj : the object
            filename : the name of the file
        Returns:
            void
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
