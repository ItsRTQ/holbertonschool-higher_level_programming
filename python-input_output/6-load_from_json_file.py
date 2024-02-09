#!/usr/bin/python3
"""module defines function load_from_json_file"""
import json


def load_from_json_file(filename):
    """this takes an obj from json file and converts it to python obj
        Return: json -> python obj
    """

    with open(filename, 'r', encoding="utf-8") as file:
        python_obj = json.loads(file.read())
    return python_obj
