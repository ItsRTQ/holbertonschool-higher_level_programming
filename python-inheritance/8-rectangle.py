#!/usr/bin/python3
"""Module defines Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle is a rectangle obj
        inherits:
            BaseGeometry
        Definitions:
            __init__: Happens as soon as the class is instanciated
    """

    def __init__(self, width, height):
        """Happends as soon the class is instanced
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
