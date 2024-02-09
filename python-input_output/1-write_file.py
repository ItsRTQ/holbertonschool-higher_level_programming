#!/usr/bin/python3
"""This module defines function write_file"""


def write_file(filename="", text=""):
    """write_file, opens a file and writes into the files"""

    with open(filename, 'w') as file:
        file.write(text)
