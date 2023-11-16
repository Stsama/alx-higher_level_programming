#!/usr/bin/python3
# 5-save_to_json_file.py
# Albert Ezoula
"""Define a function that writes a json objec in a file"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, 'w') as f:
        my_str = json.dumps(my_obj)
        f.write(my_str)
