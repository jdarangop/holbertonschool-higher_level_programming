#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        tmp = str[i]
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            tmp = chr(ord(str[i]) - 32)
        print("{}".format(tmp), end="")
    print()
