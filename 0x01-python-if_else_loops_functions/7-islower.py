#!/usr/bin/python3
def isLower(c):
    if (ord (c) >= 60 and ord(c)<=90):
        return("upper")
    elif(ord(c) >= 97 and ord(c) <= 122):
        return("lower")
    else:
        return("upper")
