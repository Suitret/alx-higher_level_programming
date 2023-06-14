#!/usr/bin/python3
"""Module containing class_to_json function
"""


def class_to_json(obj):
     """function that returns the dictionary description
        Args:
            obj : the object
        Returns:
            dict
    """
    import json
    return json.loads(obj)
