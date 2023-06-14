#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = {elem for elem in set_1 if elem in set_2}
    return (common_set)
