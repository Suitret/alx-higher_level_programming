#!/usr/bin/python3
"""Module containing inherits_from function
"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance
       of a class that inherited (directly or indirectly)
       from the specified class ; otherwise False.
        Args:
            obj : the object
            a_class : the class
        Returns:
            True or False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
