#!/usr/bin/python3
def uniq_add(my_list=[]):
    unit = set()
    resum = 0
    for num in my_list:
        if num not in unit:
            resum += num
            unit.add(num)
    
    return (resum)
