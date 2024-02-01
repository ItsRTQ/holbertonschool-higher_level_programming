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
