#!/usr/bin/python3
# 101-remove_char_at.py
# created by Albert Ezoula
def remove_char_at(str, n):
    result = str[:n] + str[n + 1:]
    return result
