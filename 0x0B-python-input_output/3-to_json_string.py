#!/usr/bin/python3
# 3-to_json_string.py
# Albert Ezoula
"""Define a function that converts a json tto string"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation
    of an object (string)
    """
    s_obj = json.dumps(my_obj)
    return (s_obj)
