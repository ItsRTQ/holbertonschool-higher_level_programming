#!/usr/bin/python3
"""Module defines Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle is a rectangle obj
        inherits:
            BaseGeometry
        Definitions:
            __init__: Happens as soon as the class is instanciated
            area():
            __str__:
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

    def area(self):
        """area calculates the area of the rectangle
            Returns:
                area of rectangle
        """

        return self.__height * self.__width

    def __str__(self):
        """This method is call when ever a instace is printed
        Returns:
            a string containing information about the obj
        """

        return f"[Rectangle] {self.__width}/{self.__height}"
