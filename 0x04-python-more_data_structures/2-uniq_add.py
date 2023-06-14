#!/usr/bin/python3
def unique_sum(input_list=[]):
    unit = set()
    resum = 0
    for num in input_list:
        if num not in unit:
            resum += num
            unit.add(num)
    
    return (resum)
