#!/usr/bin/python3
def search_replace(input_list, target, replacement):
    return [replacement if element == target else element for element in input_list]
