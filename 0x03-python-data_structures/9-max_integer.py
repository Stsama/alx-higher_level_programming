#!/usr/bin/python3
# 9-max_integer.py
# Albert Ezoula
def max_integer(my_list=[]):
    """function that finds the biggest integer of a list"""

    maxi = my_list[0]
    if my_list == []:
        return None
    for i in my_list:
        if i > maxi:
            maxi = i
    return maxi
