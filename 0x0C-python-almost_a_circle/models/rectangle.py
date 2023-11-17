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
                x(int) : the value o:7
                y(int) : the value of
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self__x = x
        self.__y = y
