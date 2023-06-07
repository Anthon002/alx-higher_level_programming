#!/usr/bin/python3
def magic_calculation(a, b, c):
    result = (c if a < b else (a + b if c > b else (a * b - c)))
    return (result)
