#!/usr/bin/python3
"""Module containing is_same_class function
"""


def is_same_class(obj, a_class):
    """function that returns True if the object is
       exactly an instance of the specified class ;
       otherwise False
        Args:
            obj : the object
            a_class : the class
        Returns:
            True or False
    """
    return isinstance(obj, a_class)
