#!/usr/bin/python3
# 6-load_from_json_file.py
# Albert Ezoula
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename) as f:
        return (json.load(f))
