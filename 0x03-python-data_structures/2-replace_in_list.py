#!/usr/bin/python3
# 2-replace_in_list.py
# Albert Ezoula
def replace_in_list(my_list, idx, element):
    """replaces an element of a list at a specific position"""

    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
