#!/usr/bin/python3
"""
Read a file
"""


def read_file(filename=""):
    """
    read a text file
    """
    with open(filename, 'r') as f:
        for line in f:
            print(line, end="")
