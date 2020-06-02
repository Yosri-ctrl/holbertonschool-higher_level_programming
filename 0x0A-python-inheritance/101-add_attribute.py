#!/usr/bin/python3
"""
add an atrribute
"""


def add_attribute(obj, str1, str2):
    """
    add str2 to str1
    """
    test = getattr(obj, "__doc__", None)
    if test is None:
        setattr(obj, str1, str2)
    else:
        raise TypeError("can't add new attribute")
