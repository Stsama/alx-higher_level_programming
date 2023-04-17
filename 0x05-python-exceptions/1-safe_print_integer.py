#!/usr/bin/python3
# 1-safe_print_integer.py
# Albert Ezoula
def safe_print_integer(value):
    """prints an integer with "{:d}".format()."""

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
