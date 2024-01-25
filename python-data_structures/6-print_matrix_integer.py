#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print()
    else:
        for row in matrix:
            for i, value in enumerate(row):
                separator = " " if i < len(row) - 1 else "\n"
                print("{:d}".format(value), end=separator)
