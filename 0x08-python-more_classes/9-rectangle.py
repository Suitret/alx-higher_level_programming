#!/usr/bin/python3
"""Module which contains Rectangle class
"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

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

        type(self).number_of_instances += 1

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

    def area(self):
        """function that computes the area
        Args:
            self : the object
        Returns:
            the area
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """function that computes the area
        Args:
            self : the object
        Returns:
            the area
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """function that returns the rectangle
        Args:
            self : the object
        Returns:
            the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            line = str(self.print_symbol) * self.__width
            res = ""
            for i in range(self.__height):
                res += line
                if i != (self.__height - 1):
                    res += "\n"
            return res

    def print(self):
        """function that returns the rectangle
        Args:
            self : the object
        Returns:
            the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            print()
        else:
            line = str(self.print_symbol) * self.__width
            for i in range(self.__height):
                print(line)

    def __repr__(self):
        """function that returns the rectangle
        Args:
            self : the object
        Returns:
            the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """function that returns the rectangle
        Args:
            self : the object
        Returns:
            void
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """function that returns the biggest rectangle
        Args:
            rect_1 : first rectangle
            rect_2 : second rectangle
        Returns:
            the biggest
        """
        flag = 0

        if isinstance(rect_1, Rectangle):
            flag += 1
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if isinstance(rect_2, Rectangle):
            flag += 1
        else:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if flag == 2:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_1.area() < rect_2.area():
                return rect_2
            else:
                return rect_1

    def square(self, size=0):
        """function that returns the squared rectangle
        Args:
            self : the object
            size : the size
        Returns:
            the squared rectangle
        """
        return Rectangle(size, size)
