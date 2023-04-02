#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# Albert Ezoula
def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order"""
    for i in reversed(len(my_list) - 1):
        print("{}".format(i))
