#!/usr/bin/python3
def add_attribute(obj, str1, str2):
    test = getattr(obj, "__doc__", None)
    if test is None:
        setattr(obj, str1, str2)
    else:
        raise TypeError("can't add new attribute")
