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

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    div_list = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg)
    for rows in matrix:
        if not isinstance(rows, list) or not rows:
            raise TypeError(msg)
        if not all(isinstance(element, (int, float)) for element in rows):
            raise TypeError(msg)
        if not len(rows) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    for rows in matrix:
        result = [round(element / div, 2) for element in rows]
        div_list.append(result)

    return div_list
