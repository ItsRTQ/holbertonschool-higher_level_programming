#!/usr/bin/python3
"""Moduele defines class Base"""
import json


class Base:
    """This class is a base for different geometrical objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method makes a dictionary into a json format string
            Return:
                string dictionary in json-format
        """

        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
