#!/usr/bin/python3
"""
check object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    object is exactly an instance of the specified class
    """
    if type(obj) == a_class:
        return True
    return False
