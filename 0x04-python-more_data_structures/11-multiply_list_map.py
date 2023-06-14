#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    final = list(map((number * lambda j: j), my_list))
    return(final)
