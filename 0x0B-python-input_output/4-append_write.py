#!/usr/bin/python3
"""
Write a string to text file at the end
"""


def append_write(filename="", text=""):
    """
    write text at the end of filename
    """
    count = 0
    with open(filename, 'a') as f:
        count = f.write(text)
    return count
