#!/usr/bin/python3
"""Square is an empty module"""


class Square:
    """define a square by it's size"""

    def __init__(self, size=0):
        """initialise the size of the square"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) != int:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
