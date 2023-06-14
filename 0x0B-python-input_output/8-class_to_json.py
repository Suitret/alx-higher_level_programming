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
    if isinstance(obj, dict):
        return obj
    json_dict = {}
    for attr, value in obj.__dict__.items():
        json_dict[attr] = value
    return json_dict
