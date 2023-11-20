#!/usr/bin/python3
# models/base.py
# Albert Ezoula
"""Define a class Base"""
import json


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
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
