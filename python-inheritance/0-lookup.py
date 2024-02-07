#!/usr/bin/python3
"""Module Defines the function lookup"""


def lookup(obj):
    """lookup, retive all the methods/attributes of obj
        Args:
            obj: object to retrive DATA off
        Returns:
            a list with all the DATA, or None if obj doesn't exist
    """

    if obj:
        return list(dir(obj))
    else:
        return None
