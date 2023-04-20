#!/usr/bin/python3
# 2-square.py
# Albert Ezoula
"""Define a class square"""


class Square:
    """Represent a Square"""

    def __init__(self, size=0):
        """initialize the square.

        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
