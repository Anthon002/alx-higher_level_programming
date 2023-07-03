#!/usr/bin/python3
"""
    This module provides 1 add_integer function
"""
def add_integer (a, b=98):
    """
    This function will add two int a and b

    Args:
        a (int):1st arg
        b (int):2nd arg

    Returns:
        int: typecasted to int if float

    Raises:
    TypeError: "a or b must be an integer"

    """
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    c = int(a) + int(b)
    return (c)
