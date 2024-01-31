#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = map(lambda x: list(map(sqr, x)), matrix)
    sqr_matrix = list(new_matrix)
    return sqr_matrix


def sqr(x):
    return x ** 2
