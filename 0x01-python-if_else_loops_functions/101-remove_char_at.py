#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str

    new_string = ""
    for i, char in enumerate(str):
        if i != n:
            new_string += char

    return new_string
