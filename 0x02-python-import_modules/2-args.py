#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = len(sys.argv) - 1
    k = 0
    if (i == 0):
        print("{} arguments.".format(i))
    elif (i > 1):
        print("{} arguments:".format(i))
    else:
        print("{} argument:".format(i))
    for j in range(i):
        k += 1
        print("{}: {}".format(k, sys.argv[k]))
