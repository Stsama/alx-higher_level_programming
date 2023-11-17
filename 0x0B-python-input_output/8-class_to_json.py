#!/usr/bin/python3
# 8-class_to_json.py
# Albert Ezoula
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """
    function that returns the dictionary
    description with simple data structure
    """
    return (obj.__dict__)
