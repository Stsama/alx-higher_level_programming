#!/usr/bin/python3
# 100-my_calculator.py
# Albert Ezoula
if __name__ == "__main__":
    """Handle basic arithmetic operations."""

    import sys

    from calculator_1 import add, sub, mul, div

    count = len(sys.argv) - 1

    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if sys.argv[2] not in list(ops.key()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = sys.argv[1]
    b = sys.argv[3]
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
