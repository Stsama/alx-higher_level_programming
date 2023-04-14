#!/usr/bin/python3
# 10-best_score.py
# Albert Ezoula
def best_score(a_dictionary):
    """ returns a key with the biggest integer value."""
    if isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    first = list(a_dictionary.key())[0]
    big = a_dictionary[first]

    for key, value in a_dictionary.items():
        if value > big:
            big = value
            first = key
    return (first)
