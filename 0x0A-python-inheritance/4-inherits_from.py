#!/usr/bin/python3
"""
object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    object is an instance of a class that inherited
    (directly or indirectly) from the specified classif issubclass
    """
    if (type(obj), a_class):
        if type(obj) != a_class:
            return True
    return False
