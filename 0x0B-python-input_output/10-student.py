#!/usr/bin/python3
"""Module containing read_file function
"""


class Student:
    """class Student that is not empty"""

    def __init__(self, first_name, last_name, age):
        """function that initializes attributes
        Args:
            self : the object
            first_name : the first name
            last_name : the last name
            age : the age
        Returns:
            void
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function that retrieves a
           dictionary representation of a Student
        Args:
            self : the object
            attrs : the authorized attributes
        Returns:
            dict
        """
        json_dict = {}
        flag = False
        if isinstance(attrs, list):
            flag = True
        for attr, value in self.__dict__.items():
            if (flag and attr in attrs) or (attrs is None):
                json_dict[attr] = value

        return json_dict
