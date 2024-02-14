#!/usr/bin/python3
"""Moduele defines class Base"""
import json
import os


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

    @classmethod
    def create(cls, **dictionary):
        """This function creates a object using a dictionary
            Returns:
                a dummy class instance
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
            dummy.update(**dictionary)
        elif cls.__name__ == "Square":
            dummy = cls(5)
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        instances_list = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                json_text = file.read()
                json_instances_list = cls.from_json_string(json_text)
            for i in json_instances_list:
                instances_list.append(cls.create(**i))
        return instances_list
