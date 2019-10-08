#!/usr/bin/python3
"""Module 2-rectangle"""


class Rectangle:
    """Rectangle

    Args: width, height

    Return: Area: area, Perimeter: perimeter
    """
    def __init__(self, width=0, height=0):
        """Init method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Area method"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter method"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)
