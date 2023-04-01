#!/usr/bin/python3
# 3-infinite_add.py
# Albert Ezoula

if __name__ == "__main__":
    """program that prints the result of the addition of all arguments"""

    import sys

    count = len(sys.argv) - 1
    total = 0
    for i in range(count):
        total += int(sys.argv[i + 1])
    print(total)
