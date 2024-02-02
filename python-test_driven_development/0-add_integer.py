#!/usr/bin/python3
"""
This Module contains the definition of add_integer()
    Definitions:
        add_integer(a, b)
"""


def add_integer(a, b=98):
    """add_integer adds a + b
    Args:
        a - First value
        b - second value

    Returns:
        The addition of a + b

    Raises:
        TypeError: When a or b arent int/float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
