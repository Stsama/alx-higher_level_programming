#!/usr/bin/python3
# 10-best_score.py
# Albert Ezoula
def best_score(a_dictionary):
    """ returns a key with the biggest integer value."""
    if a_dictionary == {}:
        return None
    top = a_dictionary[0]
    for i in a_dictionary:
        if a_dictionary[i] > top:
            top = a_dictionary[i]
    return (top)
