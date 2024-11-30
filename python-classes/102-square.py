#!/usr/bin/python3
"""
an empty Square class
"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __eq__(self, value: object):
        return self.area() == value.area()

    def __ne__(self, value: object):
        return self.area() != value.area()

    def __lt__(self, value: object):
        return self.area() < value.area()

    def __le__(self, value: object):
        return self.area() <= value.area()

    def __gt__(self, value: object):
        return self.area() > value.area()

    def __ge__(self, value: object):
        return self.area() >= value.area()