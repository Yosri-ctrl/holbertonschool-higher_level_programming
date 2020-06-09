#!/usr/bin/python3
"""
Creating Square Class unheriting from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        try:
            if "id" in kwargs:
                self.id = kwargs.get("id")
            if "size" in kwargs:
                self.__size = kwargs.get("size")
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")
            self.id = args[0]
            self.__size = args[1]
            self.x = args[2]
            self.y = args[3]
        except:
            pass

    def to_dictionary(self):
        return dict({'id': self.id, 'x': self.x, 'y': self.y,
                     'size': self.__size})
