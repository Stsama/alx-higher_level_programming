#!/usr/bin/python3
# 100-print_tebahpla.py
# created by  Albert Ezoula
for i in range(97, 123):
    if i % 2 == 0:
        i -= 32
    print("{}".format(chr(i)))

