#!/usr/bin/python3
# 0-read_file.py
# Albert Ezoula
"""Defines a text file-reading function."""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")