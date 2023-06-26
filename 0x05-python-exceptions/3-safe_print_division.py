#!/usr/bin/python3
def safe_print_division(a, b):
    x1 = None
    c = a
    d = b
    try:
        x = c / d
    except (TypeError, ZeroDivisionError):
        x = x1
    finally:
        print("Inside result: {}".format(x))
        return (x)
