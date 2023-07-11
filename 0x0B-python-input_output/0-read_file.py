#!/usr/bin/python3

"""This module contains a read_file function
"""


def read_file(filename=""):
    """
    This function reads from file filename and prints its content

    Args:
        filename: name of the file being read from
    """
    with open(filename,'r') as the_file:
        print(the_file.read())
