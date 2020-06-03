#!/usr/bin/python3
"""
Write an object JSON format to a file
"""
import json as j


def save_to_json_file(my_obj, filename):
    """
    Write my_obj to filename
    """
    with open(filename, "w+") as f:
        f.write(j.dumps(my_obj))
