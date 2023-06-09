#!/usr/bin/python3
"""Module containing Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class
        Args:
            size (int): The size of the square
            x (int): The x-coordinate of the square's position
            y (int): The y-coordinate of the square's position
            id (int): The id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute
        Args:
            value (int): The value to set as size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the square
        Args:
            *args: List of arguments
            **kwargs: Keyword arguments
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the square
        Returns:
            dict: The dictionary representation of the square
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """String representation of the square
        Returns:
            str: The string representation of the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
