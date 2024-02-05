#!/usr/bin/python3
"""
This Module contains function text_indentation()
    Definition:
        text_indentation(text)
"""


def text_indentation(text):
    """text_indentation, indentes text when .,? are found
        Args:
            text(str): text to print with indentions
        Raises:
            TypeError: when text is not a str
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    size = 0
    special_char = [".", "?", ":"]
    while size < len(text) and text[size] == ' ':
        size += 1

    while size < len(text):
        print(text[size], end="")
        if text[size] == "\n" or text[size] in special_char:
            if text[size] in special_char:
                print("\n")
            size += 1
            while size < len(text) and text[size] == ' ':
                size += 1
            continue
        size += 1

