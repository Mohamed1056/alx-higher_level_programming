#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modnum = abs(number) % 10
if (number < 0):
    modnum = -modnum
if (modnum > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, modnum))
elif (modnum == 0):
    print("Last digit of {} is {} and is 0".format(number, modnum))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, modnum))
