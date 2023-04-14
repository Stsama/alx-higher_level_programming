#!/usr/bin/python3
# 9-multiply_by_2.py
# Albert Ezoula
def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2"""

    new_dictionary = {}
    for key, value in a_dictionary:
        new_dictionary.add(a_dictionary[key]=(value * 2))
    return (new_dictionary)
