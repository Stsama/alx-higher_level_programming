#!/usr/bin/python3
# models/rectangle.py
# Albert Ezoula
"""Define a class Recangle"""
from base import Base


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
        self.width = width
        self.height = height
        selfx = x
        self.y = y
