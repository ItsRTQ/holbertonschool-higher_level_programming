#!/usr/bin/python3
"""Module defines Square"""


class Square:
    """Square is class practice"""

    def __init__(self, size=0):
        """happens as soon the class is call/use
        Args: size - size of the square

        Raises:
            TypeError: If size is not an int
            ValueError: If size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Area returns the area of the square
        Return:
            the area of the square
        """

        return self.__size * self.__size

    @property
    def size(self):
        """Size getter, use to know the size
        Returns:
            the size of the square

        Size Setter, is use to set the size or change it
            Args: value - value to be set

        Raises:
            TypeError: If size is not an int
            ValueError: If size is less than 0
        """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
