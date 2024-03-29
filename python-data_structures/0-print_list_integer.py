#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Print integers from the given list.

    Args:
        my_list (list): List of integers to be printed.

    """
    if my_list:
        for number in my_list:
            print("{:d}".format(number))
