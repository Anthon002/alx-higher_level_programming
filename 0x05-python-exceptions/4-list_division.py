#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    n_l = []
    i = 0
    while i < list_length:
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except (TypeError, IndexError):
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
            else:
                print("wrong type")
            res = 0
        finally:
            n_l.append(res)
            i += 1
    return (n_l)
