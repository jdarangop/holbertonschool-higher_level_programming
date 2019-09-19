#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tmp = list(map(lambda x: list(map(lambda x: x ** 2, x)), matrix))
    return tmp
