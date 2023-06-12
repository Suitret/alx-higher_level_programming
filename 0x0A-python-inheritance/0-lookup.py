#!/usr/bin/python3
"""Module containing lookup function
"""


def lookup(obj):
    """function that returns the list of available
       attributes and methods of an object
        Args:
            obj : the object
        Returns:
            list
    """
    return dir(obj)
