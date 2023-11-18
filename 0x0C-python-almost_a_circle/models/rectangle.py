#!/usr/bin/python3
# models/rectangle.py
# Albert Ezoula
"""Define a class Recangle"""
from models.base import Base


class Rectangle(Base):
    """Represente a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the Rectangle

            Args:
                width(int) : the width of the recantgle
                height(int) : the height of the rectangle
                x(int) : the value of
                y(int) : the value of
                id(int) : The identity of the new Rectangle.
        """
        self.width = width
        self.height = height
        selfx = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the value of the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Retrieves the value of the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Retrieves the value of the x"""
        return (x.__width)

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Retrieves the value of the y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
