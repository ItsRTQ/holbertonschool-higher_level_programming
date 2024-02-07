#!/usr/bin/python3
"""Module defines function inherits_from"""


def inherits_from(obj, a_class):
    """inherits_from determines if obj is a sub class of a_class
        Args:
            obj - obj to check
            a_class - a type/class to check if obj is
        Returns:
            True if obj is a sub class of a_class, False if not
    """

    result = type(obj) is not a_class and issubclass(type(obj), a_class)
    return result
