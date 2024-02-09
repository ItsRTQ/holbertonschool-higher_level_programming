#!/usr/bin/python3
"""this module defines function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """this function writes a obj as json string to file"""

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
