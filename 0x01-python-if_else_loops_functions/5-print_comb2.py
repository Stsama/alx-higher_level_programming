#!/usr/bin/python3
# 5-print_comb2.py
# created by Albert Ezoula
for i in range(100):
    if i == 99:
        print("{}".format(i))
    else:
        print("{:02}".format(i), end=", ")
