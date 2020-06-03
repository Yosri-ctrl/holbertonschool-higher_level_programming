#!/usr/bin/python3
"""
Return JSON representation of a file
"""
import json as j


def to_json_string(my_obj):
    """
    Return JSON representation of a file
    """
    obj = j.dumps(my_obj)
    return obj
