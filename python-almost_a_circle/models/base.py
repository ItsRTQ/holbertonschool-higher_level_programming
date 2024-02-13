#!/usr/bin/python3
"""Moduele defines class Base"""


class Base:
    """This class is a base for different geometrical objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
