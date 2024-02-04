#!/usr/bin/python3
"""
Module defines function say_my_name
    Definitions:
        say_my_name
"""


def say_my_name(first_name, last_name=""):
    """function prints My name is <first name> <last name>
        Args:
            first_name - name to print
            last_name - last name of name to print
        Raises:
            TypeError: if any first_name/last_name aren't str
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
