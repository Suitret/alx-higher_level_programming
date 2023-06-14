#!/usr/bin/python3
"""Module containing load_from_json_file function
"""


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”
        Args:
            filename : the name of the file
        Returns:
            the object
    """
    import json

    with open(filename, encoding="utf-8") as f:
        content = f.read()

    return json.loads(content)
