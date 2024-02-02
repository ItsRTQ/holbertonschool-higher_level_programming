#!/usr/bin/python3
"""
    Module defines matrix_divided
        Definitions:
            matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """matrix_divided divides all elementes by div
        Args:
            matrix - matrix to divided elements
            div - value to divided each element

        Returns:
            List with all the divitions made

        Raises:
            TypeError: When matrix is not a matrix of ints/floats
                       When Matrix have diferent size
                       When Div is not a int/float
                       When the list is empty or None is recive
            ZeroDivisionError: When div is = 0
    """

    error = TypeError("must be a matrix (list of lists) of integers/floats")
    if not matrix:
        raise error

    if not isinstance(matrix, list):
        raise TypeError("must be a matrix (list of lists) of integers/floats")

    for x in matrix:
        if not isinstance(x, list) or not x:
            raise error
        if not all(isinstance(ele, (int, float)) for ele in x):
            raise error

    if not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    lt = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))

    return lt
