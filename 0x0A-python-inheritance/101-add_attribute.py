#!/usr/bin/python3
"""Module add_attribute"""


def add_attribute(cls, attribute, value):
    """Add a new attribute if is posible"""
    if attribute in cls.__dict__.keys():
        print("entro")
        #cls.__dict__[attribute] = value
    else:
        raise TypeError('can\'t add new attribute')
