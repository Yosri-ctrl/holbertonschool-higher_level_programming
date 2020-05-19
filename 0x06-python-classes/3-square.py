#!/usr/bin/python3
"""Square is an empty module"""


class Square:
    """define a square by it's size
    and calculte it's area"""
    def __init__(self, size):
        """initialise the size"""
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

    def area(self):
        """calculte the area"""
        return self.__size * self.__size
