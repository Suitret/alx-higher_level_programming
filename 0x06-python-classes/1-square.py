#!/usr/bin/python3
"""Module which contains Square class
"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size):
        """function that initializes attributes
        Args:
            self : the object
            size (int): size of the square
        Returns:
            void
        """
        self.__size = size
