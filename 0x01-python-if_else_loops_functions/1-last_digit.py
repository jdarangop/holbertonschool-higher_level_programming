#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number < 0):
    tmp = -(-number % 10)
    print("Last digit of {} is {} and \
is less than 6 and not 0".format(number, tmp))
else:
    tmp = number % 10
    if (tmp > 5):
        print("Last digit of {} is {} and \
is greater than 5".format(number, tmp))
    elif (tmp == 0):
        print("Last digit of {} is {} and is 0".format(number, tmp))
    else:
        print("Last digit of {} is {} and \
is less than 6 and not 0".format(number, tmp))
