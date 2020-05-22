#!/usr/bin/python3
"""
print a square
"""


def print_square(size):
    """
    printing a square by a size of size
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
