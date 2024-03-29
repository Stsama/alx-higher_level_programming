#!/usr/bin/python3
# 4-print_square.py
# Albert Ezoula
def print_square(size):
    """function that prints a square with the character #
        Args:
            size (int): size length of the square
        Raises:
            TypeError : if size is not an integer
            ValueError : if size <= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
