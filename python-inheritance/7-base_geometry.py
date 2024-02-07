#!/usr/bin/python3
"""Module defines BaseGeometry"""


class BaseGeometry:
    """BaseGeometry, is a class use to validate numbers
        Definitions:
            area(): Not Implemented
            integer_validator(): validates integers
    """

    def area(self):
        """area is still not implemented
            Raises:
                Exception - when use, because is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """interger_validator, verify value
            Args:
                name: name of the value
                value: element to verify
            Raises:
                TypeError: when value is not a integer
                ValueError: when value is <= 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
