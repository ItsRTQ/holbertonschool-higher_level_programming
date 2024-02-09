#!/usr/bin/python3
"""This module defines function append_write"""


def append_write(filename="", text=""):
    """append_write, opens a file and appends into the files
        Returns: amount of character appended
    """

    with open(filename, 'a', encoding="utf-8") as file:
        charaters_appended = file.write(text)
    return charaters_appended
