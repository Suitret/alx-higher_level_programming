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
        Raises:
            TypeError: If any of the input values is not an integer
            ValueError: If any of the input values is not within the good range
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        Raises:
            TypeError: If the input is not an integer
            ValueError: If width is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        Raises:
            TypeError: If the input is not an integer
            ValueError: If height is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        Raises:
            TypeError: If the input is not an integer
            ValueError: If x is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        Raises:
            TypeError: If the input is not an integer
            ValueError: If y is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle
        Returns:
            int: The area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """Print the rectangle using '#' character
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle
        Returns:
            str: The string representation of the rectangle
        """
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle
        Args:
            *args: Non-keyword variable arguments (ignored)
            **kwargs: Keyword variable arguments (attribute/value pairs)
        """
        if args and len(args) > 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle
        Returns:
            dict: The dictionary representation of the rectangle
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
