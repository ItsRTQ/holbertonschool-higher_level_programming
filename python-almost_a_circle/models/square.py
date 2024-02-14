#!/usr/bin/python3
"""This module defines object class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class represent the geometrical shape Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """This method gets call as soon as an instance is created"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This method is call when you print a square instance"""

        msg = ""
        msg += f"[Square] ({self.id})"
        msg += f" {self.x}/{self.y}"
        msg += f" - {self.width}"
        return msg

    @property
    def size(self):
        """This the size getter, retrive the size of the square
            Return: Size of square instancet

            size setter:
                Arg:
                    Value - value to be set into size
        """
        return self.width

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("width must be > 0")
            self.width = value
            self.height = value
        else:
            raise TypeError("width must be an integer")

    def update(self, *args, **kwargs):
        """This function updates instance attributes in order based on args"""

        if args:
            for index, arg in enumerate(args, start=1):
                if index == 1:
                    self.id = arg
                elif index == 2:
                    self.width = arg
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
