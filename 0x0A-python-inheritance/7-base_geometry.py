#!/usr/bin/python3
"""
define BaseGeomtry
"""


class BaseGeometry:
    """
    define an empty method(area)
    test if the value and name are correct
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
