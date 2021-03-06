#!/usr/bin/python3
"""Module 8-rectangle"""


class Rectangle:
    """Rectangle

    Args: width, height

    Return: Area: area, Perimeter: perimeter
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Init method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = "#"

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
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """String method"""
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            string += '\n'
        return string

    def __repr__(self):
        """Representation method"""
        tm = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return tm

    def __del__(self):
        """Delection method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __ge__(self, other):
        """Greather equal method"""
        return self.area() >= other.area()

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Bigger or equal method"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1 >= rect_2:
            return rect_1
        else:
            return rect_2
