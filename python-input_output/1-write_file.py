#!/usr/bin/python3
"""This module defines function write_file"""


def write_file(filename="", text=""):
    """write_file, opens a file and writes into the files
        Returns: amount of character written
    """

    with open(filename, 'w', encoding="utf-8") as file:
        charaters_written = file.write(text)
    return charaters_written
