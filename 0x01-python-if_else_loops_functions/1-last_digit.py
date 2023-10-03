#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modnum = abs(number) % 10
if (number < 0):
    modnum = -modnum
print("Last digit of {} is {} and is ".format(number, modnum), end="")
if (modnum > 5):
    print("greater than 5")
elif (modnum == 0):
    print("0")
else:
    print("less than 6 and not 0")
