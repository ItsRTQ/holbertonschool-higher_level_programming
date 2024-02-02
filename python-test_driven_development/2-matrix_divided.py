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
            ZeroDivisionError: When div is = 0
    """

    error = TypeError("must be a matrix (list of lists) of integers/floats")
    div_list = []
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
    for x in matrix:
        results = [round(ele / div, 2) for ele in x]
        div_list.append(results)
    return div_list
