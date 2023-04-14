#!/usr/bin/python3
# 9-multiply_by_2.py
# Albert Ezoula
def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2"""
    return ({k: a_ditionary[k] * 2 for k in sorted(a_dictionary)})
