#!/usr/bin/python3
# models/base.py
# Albert Ezoula
"""Define a class Base"""
import json
import os


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
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dic = [dic.to_dictionary() for dic in list_objs]
                f.write(Base.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string == "" or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename) as f:
                list_dic = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dic]
        else:
            return []
