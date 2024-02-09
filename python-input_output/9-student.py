#!/usr/bin/python3
"""This module defines class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """This method happens as soon as a student instances is made"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """this function retrives a dictionary representation of Student obj
            Returns: dictionary
        """

        return vars(self)
