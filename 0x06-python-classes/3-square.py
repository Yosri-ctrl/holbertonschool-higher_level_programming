class Square:
    """define a square by it's size
    and calculte it's area"""
    def __init__(self, size):
        """initialise the size"""
        try:
            self.__size = size
            if size < 0:
                raise ValueError("ve")
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
    def area(self):
        """calculte the area"""
        return self.__size * self.__size
