#!/usr/bin/python3
# 9-max_integer.py
# Albert Ezoula
def max_integer(my_list=[]):
    """function that finds the biggest integer of a list"""

    if len(my_list) == 0:
        return (None)

    maxi = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maxi:
            maxi = my_list[i]

    return (maxi)
