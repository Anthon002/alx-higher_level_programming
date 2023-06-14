#!/usr/bin/python3
def find_common_elements(set_a, set_b):
    common_set = {elem for elem in set_a if elem in set_b}
    return common_set
