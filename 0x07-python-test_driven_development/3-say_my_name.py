#!/usr/bin/python3
"""Module which contains say_my_name
   function
"""


def say_my_name(first_name, last_name=""):
    """function that says the name
    Args:
        first_name : the first name
        last_name : the last name
    Returns:
        void
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
