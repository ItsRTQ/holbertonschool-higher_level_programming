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

    @classmethod
    def save_to_file(cls, list_objs):
        """This function creates a file.json based on cls and save obj"""

        filename = cls.__name__ + ".json"
        temp = []
        if list_objs and isinstance(list_objs, list):
            for i in list_objs:
                temp.append(i.to_dictionary())
        temp = cls.to_json_string(temp)
        with open(filename, 'w') as file:
            file.write(temp)

    @staticmethod
    def from_json_string(json_string):
        """This function loads a json string into a object
            Returns:
                A list
        """

        if json_string:
            return json.loads(json_string)
        else:
            return []
