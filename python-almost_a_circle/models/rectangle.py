#!/usr/bin/python3
"""This module defines class object Rectangle"""
from models.base import Base


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

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """This function is the getter for width
            Returns: instance width

            width setter:
                Arg:
                    value - value to set to instance
                Raises:
                    ValueError: if width is <= 0
                    TypeError: if width is not a int
        """

        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """This function is the getter for height
            Returns: instance height

            height setter:
                Arg:
                    value - value to set to instance
                Raises:
                    ValueError: if height is <= 0
                    TypeError: if height is not a int
        """

        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """This function is the getter for x
            Returns: instance x

            x setter:
                Arg:
                    value - value to set to instance
                Raises:
                    ValueError: if x is < 0
                    TypeError: if x is not a int
        """

        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """This function is the getter for y
            Returns: instance y

            y setter:
                Arg:
                    value - value to set to instance
                Raises:
                    ValueError: if y is < 0
                    TypeError: if y is not a int
        """

        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """this calculates and returns the area of the rectangle"""

        return self.__height * self.__width

    def display(self):
        """This functions display the rectangle using width, height, x, y"""

        for newlines in range(self.__y):
            print()
        for length in range(self.__height):
            print("{}".format(" " * self.__x), end="")
            for size in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """This method is call when you print a object instance"""

        msg = ""
        msg += f"[Rectangle] ({self.id})"
        msg += f" {self.__x}/{self.__y}"
        msg += f" - {self.__width}/{self.__height}"
        return msg

    def update(self, *args, **kwargs):
        """This function updates instance attributes in order based on args"""

        if args:
            for index, arg in enumerate(args, start=1):
                if index == 1:
                    super().__init__(int(arg))
                elif index == 2:
                    self.__width = arg
                elif index == 3:
                    self.__height = arg
                elif index == 4:
                    self.__x = arg
                elif index == 5:
                    self.__y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(value)
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """This function returns a dictionary of the rectangle instance
            Returns:
                dictionary
        """
        instance_dictionary = {'id': self.id,
                               'width': self.width,
                               'height': self.height,
                               'x': self.x,
                               'y': self.y}
        return instance_dictionary
