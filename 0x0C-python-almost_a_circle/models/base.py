#!/usr/bin/python3
"""Module containing Base class
"""


class Base:
    """Base class with private class attribute and constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class
        Args:
            id (int): Optional id for the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): List of dictionaries
        Returns:
            str: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
