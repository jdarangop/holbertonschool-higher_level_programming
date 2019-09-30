#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    tmp = [0] * list_length
    for i in range(list_length):
        try:
            tmp[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            tmp[i] = 0
        except ZeroDivisionError:
            print("division by 0")
            tmp[i] = 0
        except IndexError:
            print("out of range")
            tmp[i] = 0
    return tmp
