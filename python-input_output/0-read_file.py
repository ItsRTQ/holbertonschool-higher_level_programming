#!/usr/bin/python3
"""This module defines function read_file"""


def read_file(filename=""):
    """read_file, prints the content of file, using with"""

    with open(filename, 'r') as file:
        print(file.read(), end="")
