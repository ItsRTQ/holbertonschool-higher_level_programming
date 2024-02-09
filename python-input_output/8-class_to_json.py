#!/usr/bin/python3
"""this module defines class_to_json"""


def class_to_json(obj):
    """this funciton stringifys a python obj-instance to json-string
        Returns: class-obj attributes
    """

    return vars(obj)
