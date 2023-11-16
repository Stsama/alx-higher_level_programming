#!/usr/bin/python3
# 4-from_json_string.py
# Albert Ezoula
"""Define a string to json function"""
import json


def from_json_string(my_str):
    """function that returns an object (Python data structure)
    represented by a JSON string
    """
    obj_my_str = json.loads(my_str)
    return (obj_my_str)
