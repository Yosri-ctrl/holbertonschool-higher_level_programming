#!/usr/bin/python3
"""
print the attributs
"""


def lookup(obj):
    """
     returns the list of available attributes and methods of an object
     """
    list = [i for i in dir(obj)]
    return list
