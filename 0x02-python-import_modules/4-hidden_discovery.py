#!/usr/bin/python3
from hidden_4 import *

if __name__ == '__main__':
    tmp = dir(hidden_4)
    for i in tmp:
        if i[:2] != '__':
            print("{}".format(i))
