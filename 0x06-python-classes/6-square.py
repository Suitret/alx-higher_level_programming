#!/usr/bin/python3
"""Module which contains Square class
"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
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

        if isinstance(position[0], int) and isinstance(position[1], int):
            if len(position) == 2 and position[0] >= 0 and position[1] >= 0:
                self.__position = position
            else:
                msg = "position must be a tuple of 2 positive integers"
                raise TypeError(msg)
        else:
            msg = "position must be a tuple of 2 positive integers"
            raise TypeError(msg)

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

    @property
    def position(self):
        """function that returns the position
        Args:
            self : the object
        Returns:
            the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """function that sets a new value as position
        Args:
            self : the object
            value (tuple): new value
        Returns:
            void
        """
        if isinstance(value[0], int) and isinstance(value[1], int):
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                msg = "position must be a tuple of 2 positive integers"
                raise TypeError(msg)
        else:
            msg = "position must be a tuple of 2 positive integers"
            raise TypeError(msg)

    def my_print(self):
        """function that prints a square
        Args:
            self : the object
        Returns:
            void
        """
        char = '#' * self.__size
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            print(char)
        if self.__size == 0:
            print()
