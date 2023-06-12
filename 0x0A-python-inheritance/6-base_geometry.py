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
