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
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")
