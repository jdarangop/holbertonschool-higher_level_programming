#!/usr/bin/python3
def print_last_digit(number):
    tmp = str(number)
    tmp = tmp[-1]
    tmp = int(tmp)
    print(tmp, end="")
    return tmp
