#!/usr/bin/python3
# 1-rectangle.py
# Albert Ezoula
"""define a rectangle class"""


class Rectangle:
    """represent the rectangle class"""

    def __init__(self, width=0, height=0):
        """Initilisation of the square"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """retrieves the value of the height"""
        return (self.__height)

    @property
    def width(self):
        """retrieves the value of the width"""
        return (self.__width)

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
