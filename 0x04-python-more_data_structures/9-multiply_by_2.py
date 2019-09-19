#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for i in new_dict.keys():
        tmp = new_dict.get(i)
        new_dict[i] = tmp * 2
    return new_dict
