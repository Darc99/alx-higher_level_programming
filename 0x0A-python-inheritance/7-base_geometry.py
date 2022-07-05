#!/usr/bin/python3
"""Creates a BaseGeometry class."""


class BaseGeometry:
    """
    Public instance method that raises an exception
    """
    def area(self):
        """Not yet impl"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
