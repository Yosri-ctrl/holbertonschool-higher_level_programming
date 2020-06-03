#!/usr/bin/python3
"""
Return python object represented by JSON
"""
import json as j


def from_json_string(my_str):
    """
    Return python object represented by JSON
    """
    obj = j.loads(my_str)
    return obj
