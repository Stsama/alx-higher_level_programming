#!/usr/bin/python3
# models/base.py
# Albert Ezoula
"""DDefine a class Base"""


class Base:
    """Represent the Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of a class Base
            Args:
                id(int): The id of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
