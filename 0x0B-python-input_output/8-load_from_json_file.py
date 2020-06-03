#!/usr/bin/python3
"""
Creat an object from JSON file
"""
import json as j


def load_from_json_file(filename):
    """
    Creat An obj from filename
    """
    with open(filename, 'r') as f:
        return j.load(f)
