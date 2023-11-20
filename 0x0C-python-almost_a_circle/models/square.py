#!/usr/bin/python3
# models/square.py
# Albert Ezoula
"""Define the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent the square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        a = f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} "
        b = f"- {self.width}"
        return a + b
