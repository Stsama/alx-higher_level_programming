#!/usr/bin/python3
# 3-print_alphabt.py
# create by Albert EZOULA

for letter in range(97, 123):
    if letter == 101 or letter == 113:
        continue
    print(chr(letter), end="")
