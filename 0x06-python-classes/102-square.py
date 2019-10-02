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
        self.size = size

    def area(self):
        """Area of the square method.

        Returns:
            Area.

        """
        return self.__size ** 2

    @property
    def size(self):
        """size of the side.

        Returns:
            self.__size.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter function.

        Args:
            value: value for size atributte.

        Returns:
            None.

        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def __lt__(self, other):
        """size setter function.

        Args:
            value: value for size atributte.

        Returns:
            None.

        """
        return self.size < other.size

    def __le__(self, other):
        """size setter function.

        Args:
            value: value for size atributte.

        Returns:
            None.

        """
        return self.size <= other.size

    def __eq__(self, other):
        """size setter function.

        Args:
            value: value for size atributte.

        Returns:
            None.

        """
        return self.size == other.size

    def __ne__(self, other):
        """size setter function.

        Args:
            value: value for size atributte.

        Returns:
            None.

        """
        return self.size != other.size

    def __gt__(self, other):
        """size setter function.

        Args:
            value: value for size atributte.

        Returns:
            None.

        """
        return self.size > other.size

    def __ge__(self, other):
        """size setter function.

        Args:
            value: value for size atributte.

        Returns:
            None.

        """
        return self.size >= other.size
