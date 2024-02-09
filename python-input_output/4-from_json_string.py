#!/usr/bin/python3
"""this module defines function from_json_string"""
import json


def from_json_string(my_str):
    """this function takes a json stringify transforms it obj back to an obj
        Returns: obj
    """

    python_obj = json.loads(my_str)
    return python_obj
