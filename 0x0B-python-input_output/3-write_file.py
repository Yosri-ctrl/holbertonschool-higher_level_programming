#!/usr/bin/python3
"""
Write a string to text file
"""


def write_file(filename="", text=""):
    """
    write text in filename
    """
    count = 0
    with open(filename, 'w') as f:
        count = f.write(text)
    return count