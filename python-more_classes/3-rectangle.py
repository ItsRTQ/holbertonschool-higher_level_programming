#!/usr/bin/python3
"""Module defines class name Rectangle that instances a rectangle"""


class Rectangle:
    """Rectangle, does nothing right now
        Definitions:
            __init__: happens when instances of Rectangle is created
            width(): getter/setter for self.width
            height(): getter/setter for self.height
    """

    def __init__(self, width=0, height=0):
        """Happends as soon the class is instanced
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
                TypeError: when value is not int
                ValueError: when value is not >= 0
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def height(self):
        """height, is a function that retrive height

            height setter:
                Arg:
                    value - value to set to self.height
                Raises:
                    Raises:
                        TypeError: when value is not int
                        ValueError: when value is not >= 0
        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """width, is a function that retrives width

            width setter:
                Arg:
                    value - value to set to self.width
                Raises:
                    TypeError: when value is not int
                    ValueError: when value is not >= 0
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """area calculates the area of the rectangle
            Returns:
                area of rectangle
        """

        return self.__height * self.__width

    def perimeter(self):
        """perimeter calculates the perimeter of the rectangle
            Returns:
                perimeter of rectangle
        """

        peri = 2 * (self.__height + self.__width)
        if self.__height == 0 or self.__width == 0:
            peri = 0
        return peri

    def __str__(self):
        """prints the rectangle when object is printed
            Return: the rectangle printed
        """

        rect_printed = ""
        for size in range(self.__height):
            for length in range(self.__width):
                rect_printed += "#"
            rect_printed += "\n"
        return rect_printed.rstrip("\n")
