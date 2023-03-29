#!/usr/bin/python3
# 12-fizzbuzz.py
# created by Albert Ezoula
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(i), end="")