#!/usr/bin/python3
def search_replace(input_list, target, replacement):
    return [replacement if i == target else i for i in input_list]
