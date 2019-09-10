#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

tmp = str(number)
tmp = tmp[-1]
tmp = int(tmp)
if (number > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, tmp))
elif (number == 0):
    print("Last digit of {} is {} and is 0".format(number, tmp))
elif (number < 6 and number != 0):
    print("Last digit of {} is {} and \
is less than 6 and not 0".format(number, tmp))
