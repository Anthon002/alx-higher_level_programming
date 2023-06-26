#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    k = 0
    j = 0
    while True:
        try:
            print("{}".format(my_list[j]), end="")
            k += 1
            j += 1
            if k == x:
                break
        except IndexError:
            break
    print("")
    return (k)
