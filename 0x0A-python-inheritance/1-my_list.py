#!/usr/bin/python3
"""Module which contains MyList class
"""


class MyList(list):
    """class MyList that defines a list"""

    def __init__(self):
        """function that initializes attributes
        Args:
            self : the object
        Returns:
            void
        """
        super().__init__(self)

    def print_sorted(self):
        """function that prints the list
           but sorted (ascending sort)
        Args:
            self : the object
        Returns:
            void
        """
        temp = self.copy()
        temp.sort()
        print(temp)
