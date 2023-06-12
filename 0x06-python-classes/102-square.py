#!/usr/bin/python3
"""Module which contains Square class
"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """function that initializes attributes
        Args:
            self : the object
            size (int): size of the square
        Returns:
            void
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """function that computes the area of a square
        Args:
            self : the object
        Returns:
            area (int)
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """function that returns the size
        Args:
            self : the object
        Returns:
            the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """function that sets a new value as size
        Args:
            self : the object
            value (int): new value
        Returns:
            void
        """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def __eq__(self, other):
        """function that checks if equal
        Args:
            self : the object
            value : new value
        Returns:
            void
        """
        return self.area() == other.area()

    def __gt__(self, other):
        """function that checks if greater
        Args:
            self : the object
            value : new value
        Returns:
            void
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """function that checks if greater or equal
        Args:
            self : the object
            value : new value
        Returns:
            void
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """function that checks if lesser
        Args:
            self : the object
            value : new value
        Returns:
            void
        """
        return self.area() < other.area()

    def __le__(self, other):
        """function that checks if lesser or equal
        Args:
            self : the object
            value : new value
        Returns:
            void
        """
        return self.area() <= other.area()

    def __ne__(self, other):
        """function that checks if different
        Args:
            self : the object
            value : new value
        Returns:
            void
        """
        return self.area() != other.area()
