#!/usr/bin/python3
from calculator_1 import *
if __name__ == "__main__":
    def calculate_all():
        a = 10
        b = 5
        c =[add(a, b), sub(a, b), mul(a, b), div(a, b)]
        for i in range(len(c)):
            print("{} + {} = {}".format(a, b, c[i]))
    calculate_all()
