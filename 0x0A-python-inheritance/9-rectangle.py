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
            void
        """
        raise Exception("area() is not implemented")

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
            temp = name + " must be an integer"
            raise TypeError(temp)

        if value <= 0:
            temp = name + " must be greater than 0"
            raise ValueError(temp)


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
        super().integer_validator(self, "width", width)
        self.__width = width
        super().integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        """function that raises an exception
        Args:
            self : the object
        Returns:
            area
        """
        return self.__width * self.__lenght

    def __str__(self):
        """function that returns attributes
           of the rectangle
        Args:
            self : the object
        Returns:
            void
        """
        rect = "[Rectangle] "
        rect += (str(self.__width) + "/" + str(self.__height))
        return rect
