#!/usr/bin/python3
"""Module defines Square"""


class Square:
    """Square is class practice"""

    def __init__(self, size=0, position=(0, 0)):
        """happens as soon the class is call/use
        Args:
            size - size of the square
            position - position of the cube

        Raises:
            TypeError: When size is not int or position not a tuple, 2 int >= 0
            ValueError: If size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(xy < 0 for xy in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    def my_print(self):
        """my_print, prints the cube based on its size and position"""

        if self.__size > 0:
            for i in range(self.__size):
                for spaces in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        """position getter, Retrive the value of position
            Returns:
                the position of the square
            position setter, sets or changes position value
                Args: value - value to set to position
        """

        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(xy < 0 for xy in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
