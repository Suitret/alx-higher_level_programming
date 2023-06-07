#!/usr/bin/python3
"""This module contains addition function
"""


def add_integer(a, b=98):
    """function that adds two values"""
    flag = 0

    if isinstance(a, int) or isinstance(a, float):
        flag += 1
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, int) or isinstance(b, float):
        flag += 1
    else:
        raise TypeError("b must be an integer")

    if flag == 2:
        a, b = int(a), int(b)
        return (a + b)
