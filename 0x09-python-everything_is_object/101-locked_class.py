#!/usr/bin/python3
"""Module containing LockedClass"""


class LockedClass:
    """This is the LockedClass"""

    __slots__ = ('first_name')

    def __setattr__(self, name, value):
        """function to authorize dynamic
           attribute
           Args:
               self : the object
               name : the attribute name
               value : the attribute value
           Return:
               void
        """

        if hasattr(self, name):
            super().__setattr__(name, value)
