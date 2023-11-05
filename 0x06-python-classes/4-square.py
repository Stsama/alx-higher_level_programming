#!/usr/bin/python3
# 3-square.py
# Albert Ezoula
""" defines a class square"""


class Square:
    """represent a square"""
    def __init__(self, size=0):
        """Initialize a new square.


        Arg:
            size(int): The size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = self.size = size

    @property
    def size(self):
        """Retrieves size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""

        return (self.__size ** 2)
