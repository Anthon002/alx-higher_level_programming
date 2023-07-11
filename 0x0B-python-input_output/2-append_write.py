#!/usr/bin/python3

"""
This module contains the funtion append_write()
"""

def append_write(filename="", text=""):
    """
    This function appends to the filename file
    """
    with open(filename, 'a', encoding='utf-8') as the_file:
        the_file.write(text)
    return(len(text))
