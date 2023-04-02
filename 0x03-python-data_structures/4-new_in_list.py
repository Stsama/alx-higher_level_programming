#!/usr/bin/python3
# 4-new_in_list.py
# Albert Ezoula
def new_in_list(my_list, idx, element):
    """ replaces an element in a list without modifying the original list"""
    new_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
