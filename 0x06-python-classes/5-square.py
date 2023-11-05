#!/usr/bin/python3
# 5-square.py
# Created by Albert Ezoula
"""module that difine a class"""


class Square:
    """class that represent a square"""

    def __init__(self, size=0):
        """Initialisationof the square class

        Args:
            size(int): The size of a square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = self.size = size

    @property
    def size(self):
        """retrieves the value of size"""
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
        """calculates and retrieves the value of the square area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
