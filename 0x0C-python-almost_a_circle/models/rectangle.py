#!/usr/bin/python3
"""
Creating the class rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    defintion of a Rectangle
    define a width and a height
    and a position by x, y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.__x, self.__y,
                                                        self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        try:
            if "id" in kwargs:
                self.id = kwargs.get("id")
            if "width" in kwargs:
                self.__width = kwargs.get("width")
            if "height" in kwargs:
                self.__height = kwargs.get("height")
            if "x" in kwargs:
                self.__x = kwargs.get("x")
            if "y" in kwargs:
                self.__y = kwargs.get("y")
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except:
            pass

    def to_dictionary(self):
        return dict({'x': self.__x, 'y': self.__y, 'id': self.id,
                     'height': self.__height, 'width': self.__width})
