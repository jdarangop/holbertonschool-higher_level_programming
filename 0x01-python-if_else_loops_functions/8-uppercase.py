#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (ord(str[i]) >= 65 and ord(str[i]) <= 90):
            if ord(str[i]) >= 97 and ord(str[i]) <= 122:
                tmp = chr(ord(str[i]) - 32)
            else:
                tmp = str[i]
        elif (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            if ord(str[i]) >= 97 and ord(str[i]) <= 122:
                tmp = chr(ord(str[i]) - 32)
            else:
                tmp = str[i]
        else:
            tmp = str[i]
        print(tmp, end="")
    print()
