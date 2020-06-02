#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
class Square that inherits from Rectangle
"""


class Square(Rectangle):
    """
    define a square
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
