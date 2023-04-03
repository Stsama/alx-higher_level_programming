#!/usr/bin/python3
# 10-divisible_by_2.py
# Albert Ezoula
def divisible_by_2(my_list=[]):
    """function that finds all multiples of 2 in a list"""

    new_list = []
    for i in range(len(my_list)):
        new_list.append(my_list[i] % 2 == 0)

    return new_list
