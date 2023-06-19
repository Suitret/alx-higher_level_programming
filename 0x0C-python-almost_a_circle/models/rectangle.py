#!/usr/bin/python3
"""Module containing Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle class
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x-coordinate of the rectangle's position
            y (int): The y-coordinate of the rectangle's position
            id (int): The id of the rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute
        Args:
            value (int): The value to set as width
        """
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute
        Args:
            value (int): The value to set as height
        """
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute
        Args:
            value (int): The value to set as x
        """
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute
        Args:
            value (int): The value to set as y
        """
        self.__y = value
