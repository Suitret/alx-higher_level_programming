#!/usr/bin/python3
"""Module containing to_json_string function
"""


def to_json_string(my_obj):
    """function that returns the JSON representation
       of an object (string)
        Args:
            my_obj : the object
        Returns:
            json form of a string
    """
    import json
    return json.dumps(my_obj)
