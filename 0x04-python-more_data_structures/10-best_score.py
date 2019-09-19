#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    keys = list(a_dictionary.keys())
    maximo = a_dictionary[keys[0]]
    for i in a_dictionary.keys():
        tmp = a_dictionary.get(i)
        if tmp is None:
            return None
        if tmp > maximo:
            maximo = tmp
            key = i
    return key
