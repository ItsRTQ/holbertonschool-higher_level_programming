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

    skip = False
    result = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i, char in enumerate(text):
        skip = False
        result += char
        if char in ["?", ".", ":"]:
            result += "\n\n"

    for sentence in result.split('\n'):
        print(sentence.strip())
