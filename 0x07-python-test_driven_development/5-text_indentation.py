#!/usr/bin/python3
"""This module contains one funtion text_indentation()."""


def text_indentation(text):
    """This function prints out text with indentation after '.', '?',':'.

    Args:
        text (str): The text to be indented.
    Raises:
        TypeError: if the text is not a string.
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    count = 0
    ln_txt = len(text)
    while count < ln_txt and text[count] == ' ':
        count += 1

    while count < ln_txt:
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count += 1
            while count < ln_txt and text[count] == ' ':
                count += 1
            continue
        count += 1
