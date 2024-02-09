#!/usr/bin/python3
"""this module defines pascal_triangle"""


def pascal_triangle(n):
    """this function returns a pascal list size of n
        Returns: list of lists
    """

    pascal = []
    if n <= 0:
        return pascal
    for amount, row in enumerate(range(n), start=1):
        pascal_row = []
        for elements in range(amount):
            if elements == 0 or elements+1 == amount:
                pascal_row.append(1)
            else:
                pascal_row.append(temp[elements] + temp[elements-1])
        pascal.append(pascal_row.copy())
        temp = pascal_row.copy()

    return pascal
