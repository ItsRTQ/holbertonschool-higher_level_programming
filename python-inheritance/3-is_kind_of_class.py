#!/usr/bin/python3
"""Module defines function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class, determines if obj is an instance of a_class
        Args:
            obj - obj to check
            a_class - a type/class to check if obj is
        Returns:
            True if obj is of same type of a_class, False if not
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
