#!/usr/bin/python3
"""This module defines class object Rectangle"""
from base import Base


class Rectangle(Base):
    """This object represents the geometrical shape of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """This function is the getter for width
            Returns: instance width

            width setter: is use to set/overwrite instance width
        """

        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """This function is the getter for height
            Returns: instance height

            width setter: is use to set/overwrite instance height
        """

        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """This function is the getter for x
            Returns: instance x

            width setter: is use to set/overwrite instance x
        """

        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """This function is the getter for y
            Returns: instance y

            width setter: is use to set/overwrite instance y
        """

        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
