#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if str[i].isalpha():
            if ord(str[i]) >= 97 and ord(str[i]) <= 122:
                str[i] = chr(ord(str[i]) - 32)
