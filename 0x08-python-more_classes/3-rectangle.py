#!/usr/bin/python3
# 3-rectangle.py
# Albert Ezoula
"""Define a rectangle class"""


class Rectangle:
    """Represente a rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of a rectangle
            height (int) : The height of a rectangle
        """
        self.__height = height
        self.__width = width

    def __str__(self):
        """should print the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return("".join(rect))

    @property
    def height(self):
        """Retrieves the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)
