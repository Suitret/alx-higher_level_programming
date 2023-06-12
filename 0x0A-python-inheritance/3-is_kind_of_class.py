#!/usr/bin/python3
"""Module containing is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is
       exactly an instance of the specified class ,
       or if the object is an instance of a class
       that inherited from, the specified class ;
       otherwise False
        Args:
            obj : the object
            a_class : the class
        Returns:
            True or False
    """
    return isinstance(obj, a_class) or issubclass(obj, a_class)
