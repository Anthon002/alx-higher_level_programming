#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
def hand():
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        operas = {
        "+": (add, "+"),
        "-": (sub, "-"),
        "*": (mul, "*"),
        "/": (div, "/")
        }
        opera = sys.argv[2]
        if opera not in operas:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

            a = int(sys.argv[1])
            b = int(sys.argv[3])
            result = operas[opera][0](a, b)
            opera_symbol = operas[opera][1]
            print("{} {} {} = {}".format(a, opera_symbol, b, result))


if __name__ == "__main__":
    hand()
