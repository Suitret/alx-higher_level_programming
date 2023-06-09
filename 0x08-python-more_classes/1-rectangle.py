#!/usr/bin/python3
"""Module which contains Rectangle class
"""


class Rectangle:
    """class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """function that initializes attributes
        Args:
            self : the object
            width (int): width of the rectangle
            height (int): height of the rectangle
        Returns:
            void
        """
        if isinstance(width, int):
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """function that returns the width
        Args:
            self : the object
        Returns:
            the width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """function that sets the width
        Args:
            self : the object
            width (int): the width
        Returns:
            void
        """
        if isinstance(width, int):
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """function that returns the height
        Args:
            self : the object
        Returns:
            the height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """function that sets the height
        Args:
            self : the object
            height (int): the height
        Returns:
            void
        """
        if isinstance(height, int):
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
