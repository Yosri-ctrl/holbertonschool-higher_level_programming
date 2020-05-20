#!/usr/bin/python3
"""Square is an empty module"""


class Square:
    """define a square by it's size"""

    def __init__(self, size=0, position=(0, 0)):
        """initialise the size of the square"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        #print(self.__position)
        if self.__size == 0:
            print("")
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print("")

        for i in range(self.__size):
            if self.__position[0] > 0:
                print(" " * self.__position[0], end="") 
            print("#" * self.__size)
