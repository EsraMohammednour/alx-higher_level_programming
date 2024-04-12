#!/usr/bin/python3
"""
saroo
"""


class Student:
    """
    A class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        init
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        to json
        """
        return self.__dict__.copy()
