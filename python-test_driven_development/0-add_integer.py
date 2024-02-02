#!/usr/bin/python3
"""This Module contains the definition of add_integer()"""


def add_integer(a, b=98):
    """add_integer adds a + b
    Args:
        a - First value
        b - second value

    Returns:
        The addition of a + b

    Raises:
        TypeError: When a or b arent int or float
    """

    result = 0
    if isinstance(a, (int, float)):
        result += int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        result += int(b)
    else:
        raise TypeError("b must be an integer")
    return result
