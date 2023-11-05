#!/usr/bin/python3
# 6-square.py
# created by  Albert Ezoula
"""Define a squarer class"""


class Square:
    """class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialisation of the Square

        Args:
            size(int): Reprensent the size of the square
            position(tuple): represent the position of an area
        Raises:
            TypeError: if size is not an integer
            ValueError: if value is LESS than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = self.size = size
        self.__position = position

    @property
    def size(self):
        """retrieves the value of the square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the value of the square size"""
        self.__size = value

    def area(self):
        """calculates and retrieves the area of the square"""
        return (self.__size ** 2)

    @property
    def position(self):
        """retrieves the position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets the position of a the square"""
        if not isinstance(value, tuple) and len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] <= 0 and value[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            print("{}".format(" " * self.__position[0]), end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
