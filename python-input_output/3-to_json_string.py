#!/usr/bin/python3
"""this module defines function to_json_string"""
import json


def to_json_string(my_obj):
    """this function stringifys a obj to json txt
        Returns: the stringify data
    """

    as_json = json.dumps(my_obj)
    return as_json
