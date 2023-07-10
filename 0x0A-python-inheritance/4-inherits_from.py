#!/usr/bin/python3
"""This module contains the inherits_from() function
"""


def inherits_from(obj, a_class):
    """This function checks if an object is an instance of a class that inherited from the class
    """
    if type(obj) == a_class:
        return (False)
    else:
        tof = issubclass(type(obj), a_class)
        return (tof)

