#!/usr/bin/python3
"""Module which contains BaseGeometry class
"""


class BaseGeometry:
    """class BaseGeometry that is empty"""

    def area(self):
        """function that raises an exception
        Args:
            self : the object
        Returns:
            area
        """
        return self.__width * self.__lenght

    def integer_validator(self, name, value):
        """function that validates value
        Args:
            self : the object
            name (string): the name
            value (int): the value
        Returns:
            void
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """class Rectangle that is not empty"""

    def __init__(self, width, height):
        """function that initializes attributes
        Args:
            self : the object
            width : the width
            height : the height
        Returns:
            void
        """
        super().integer_validator(self, "", width)
        self.__width = width
        super().integer_validator(self, "", height)
        self.__height = height

    def __str__(self):
        """function that returns attributes
           of the rectangle
        Args:
            self : the object
        Returns:
            void
        """
        rect = "[Rectangle] "
        rect += str(self.__width) + "/" + str(self.__height)
