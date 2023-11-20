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

    @property
    def size(self):
        """retrieves the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes:"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
