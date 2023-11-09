#!/usr/bin/python3
# 1-my_list.py
# Created by Albert Ezoula
"""module that difine a class"""


class MyList(list):
    """represent the class Mylist"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
