#!/usr/bin/python3
""" This module contains the write_file function
"""

def write_file(filename="", text=""):
    """
    This function writes to the filename file
    
    Args: 
        filename(str): name of the file to be read from
        text(str): what to write to the file

    Return: length of text
    """
    with open(filename, 'w', encoding = "utf-8") as the_file:
        the_file.write(text)
    return (len(text))
