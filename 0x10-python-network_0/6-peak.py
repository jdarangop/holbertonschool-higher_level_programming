#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ Function """
    if list_of_integers is None or list_of_integers == []:
        return None
    numbers = list_of_integers
    left = 0
    right = len(numbers) - 1
    while left < right:
        mid = int((left + right)/2)
        if numbers[mid] < numbers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return numbers[left]
