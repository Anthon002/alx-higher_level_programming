#!/usr/bin/python3

"""this module has a is_same_class() function """

def is_same_class(obj, a_class):
    """
    is_same_class checks if obj is the same type as a_class
    """
    tof = True
    if (type(obj) == a_class):
        tof = True
    else:
        tof = False
    return (tof)
