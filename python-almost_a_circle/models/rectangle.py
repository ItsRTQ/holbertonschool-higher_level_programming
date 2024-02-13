#!/usr/bin/python3
"""This module defines class object Rectangle"""
from base import Base


class Rectangle(Base):
    """This object represents the geometrical shape of a rectangle
        Definitions:
            width(): getter/setter
            height(): getter/setter
            x(): getter/setter
            y(): getter/setter
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """This happens as soon as a rectangle instancen is created
            Args:
                width: width of rectangle
                height: height of rectangle
                x: x position of rectangle
                y: y position of rectangle
                id: id of rectangle
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """This function is the getter for width
            Returns: instance width

            width setter:
                Arg:
                    value - value to set to instance
        """

        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """This function is the getter for height
            Returns: instance height

            height setter:
                Arg:
                    value - value to set to instance
        """

        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """This function is the getter for x
            Returns: instance x

            x setter:
                Arg:
                    value - value to set to instance
        """

        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """This function is the getter for y
            Returns: instance y

            y setter:
                Arg:
                    value - value to set to instance
        """

        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
