#!/usr/bin/python3
"""Square is an empty module"""


class Square:
    """Define a square by it's size"""
    def __init__(self, size=0):
        """initialise the size value
        args:
            size: size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
