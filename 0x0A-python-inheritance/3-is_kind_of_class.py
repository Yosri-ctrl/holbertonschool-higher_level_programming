#!/usr/bin/python3
"""
check object is an instance of, or if the object is an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    object is an instance of, or if the object is an instance of a class that inherited from
    """
    if issubclass(type(obj), a_class):
        return True
    return False
