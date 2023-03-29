#!/usr/bin/python3
# created by Albert Ezoula
def print_last_digit(number):
    result = abs(number)
    c = result % 10
    if number < 0:
        c  *= -1
    return c

