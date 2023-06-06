#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numToStr = str(number)
bakToNum = int(numToStr[-1])
if (number < 0):
    bakToNum = bakToNum * (-1)
if (bakToNum > 5):
    print(f"Last digit of {number} is {bakToNum} and is greater than 5")
elif(bakToNum == 0):
    print(f"Last digit of {number} is {bakToNum} and is 0")
else:
    print(f"Last digit of {number} is {bakToNum} and is less than 6 and not 0")
