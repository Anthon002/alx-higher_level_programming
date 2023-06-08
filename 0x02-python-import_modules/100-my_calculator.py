#!/usr/bin/python3
from calculator_1 import *
import sys
if __name__ == "__main__":
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    oprato = {"/": div, "-": sub, "+": add, "*": mul}
    if sys.argv[2] not in list(oprato.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, oprato[sys.argv[2]](a, b)))
