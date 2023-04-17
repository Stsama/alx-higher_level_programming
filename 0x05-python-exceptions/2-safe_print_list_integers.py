#!/usr/bin/python3
# 2-safe_print_list_integers.py
# Albert Ezoula
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers."""
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (ret)
