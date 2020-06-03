#!/usr/bin/python3
"""
Count the lines in a file
"""


def number_of_lines(filename=""):
    """
    Return the number of lines in filename
    """
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += 1
    return count
