#!/usr/bin/python3
"""Module defines class square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square is a object template for a square
    Definitions:
        __init__: Happens as soon as an instance is created
    """

    def __init__(self, size):
        """This methos is call as soon as obj instance is created
            Args:
                size: size of the square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area returns the area of the square
        Return:
            the area of the square
        """

        return self.__size * self.__size
