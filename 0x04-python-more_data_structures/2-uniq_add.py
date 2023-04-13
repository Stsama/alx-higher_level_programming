#!/usr/bin/python3
# 2-uniq_add.py
# Albert Ezoula
def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)"""
    addition = 0
    for x in set(my_list):
        addition += x
    return (addition)
