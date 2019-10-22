#!/usr/bin/python3
"""Module Square"""
from models.rectangle import Rectangle
import json


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init method"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Width getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Width setter"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update method"""
        attributes = ["id", "size", "x", "y"]
        if args is not None:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        if len(args) == 0 or args[0] == "":
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """To dictionary method"""
        attributes = ["id", "size", "x", "y"]
        values = [self.id, self.size, self.x, self.y]
        return dict(zip(attributes, values))
