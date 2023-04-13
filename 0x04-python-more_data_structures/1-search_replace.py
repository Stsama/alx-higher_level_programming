#!/usr/bin/python3
# 1-search_replace.py
# Albert Ezoula
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list"""

    for item in range(len(my_list)):
        if my_list[item] == search:
            my_list[item] = replace
    return my_list
