#!/usr/bin/python3
"""This module defines class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """This method happens as soon as a student instances is made"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """this function retrives a dictionary representation of Student obj
            Returns: dictionary
        """

        Student_dict = vars(self)
        wanted_data = {}
        if isinstance(attrs, list):
            for key in attrs:
                if isinstance(key, str) and key in Student_dict:
                    wanted_data[key] = Student_dict[key]
            return wanted_data
        return Student_dict

    def reload_from_json(self, json):
        """This function reloads Student instance"""

        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
