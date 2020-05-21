#!/usr/bin/python3
"""Square is an empty module"""


class Square:
    """define a square by it's size"""

    def __init__(self, size=0, position=(0, 0)):
        """initialise the size of the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        if not type(size) == int:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        mess = "position must be a tuple of 2 positive integers"
        if type(value) != tuple or len(value) != 2:
            raise TypeError(mess)
        if type(value[1]) != int or type(value[0]) != int:
            raise TypeError(mess)
        if value[0] < 0 or value[1] < 0:
            raise TypeError(mess)
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        square = ""
        if self.__size == 0:
            square += "\n"
            return square
        for i in range(self.__position[1]):
            square += "\n"

        for i in range(self.__size):
            if self.__position[0] > 0:
                square += " " * self.__position[0]
            square += "#" * self.__size
        square += "\n"
        return square