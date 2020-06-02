#!/usr/bin/python3
"""
define a Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    initilise the size
    """
    def __init__(self, size):
        super().__init__(size, size)
