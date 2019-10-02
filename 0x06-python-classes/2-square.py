#!/usr/bin/python3


class Square:
    """Square.

    Attributes:
        size (int): size of the side of the square.

    """
    def __init__(self, size=0):
        """__init__ function.

        Args:
            size: size of the side of the square.

        Returns:
            None.

        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
