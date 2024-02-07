#!/usr/bin/python3
"""Module defines funtion is_same_class"""


def is_same_class(obj, a_class):
    """is_same_class, determines if obj is type a_class
        Args:
            obj - obj to check
            a_class - a type/class to check if obj is
        Returns:
            True if obj is of same type of a_class, False if not
    """

    result = type(obj) is a_class
    return result
