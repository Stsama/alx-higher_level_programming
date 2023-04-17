#!/usr/bin/python3
# 3-safe_print_division.py
# Albert Ezoula
def safe_print_division(a, b):
    """divides 2 integers and prints the result."""

    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
