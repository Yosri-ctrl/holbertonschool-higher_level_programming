#!/usr/bin/python3
class Square:
    """Define a square by it's size"""
    def __init__(self, size=0):
        """initialise the size value"""
        try:
            self.__size = size
            if size < 0:
                raise ValueError("ve") 
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
    