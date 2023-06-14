#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    nume = sum(elem[0] * elem[1] for elem in my_list)
    denom = sum(elem[1] for elem in my_list)
    return (nume / denom)
