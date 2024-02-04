#!/usr/bin/python3
"""
Module defines print_square()
    Definitions:
        print_square(size)
"""


def print_square(size):
    """print_square, prints a square based on size
        Args:
            size(int): the size for square
        Raises:
            TypeError: if size is not a integer
            ValueError: when size is not >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for block in range(size):
        for rows in range(size):
            print("#", end="")
        print()
