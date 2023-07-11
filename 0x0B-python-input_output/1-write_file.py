#!/usr/bin/python3
""" This module contains the write_file function
"""

def write_file(filename="", text=""):
    with open(filename, 'w', encoding = "utf-8") as the_file:
        the_file.write(text)
    return (len(text))
