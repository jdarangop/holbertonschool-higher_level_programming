#!/usr/bin/python3


class Square:
    """Square.

    Attributes:
        size (int): size of the side of the square.
        position (tuple): Position of the square printed.

    """
    def __init__(self, __size=0, __position=(0, 0)):
        """__init__ function.

        Args:
            size: size of the side of the square.
            position: Position of the square printed.

        Returns:
            None.

        """
        self.size = __size
        self.position = __position

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
            return
        elif value < 0:
            raise ValueError('size must be >= 0')
            return
        else:
            self.__size = value

    def my_print(self):
        """my_print Print the square.

        Returns:
            None.

        """
        x = self.__size
        pos = self.__position

        if x == 0:
            print()
            return

        for k in range(pos[1]):
            print()

        for i in range(x):
            print(' ' * pos[0], end='')
            for j in range(x):
                print('#', end='')
            print()

    @property
    def position(self):
        """position of the square.

        Returns:
            self.__position.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter function.

        Args:
            value: value for position atributte.

        Returns:
            None.

        """

        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
            return
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
            return
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
            return
        else:
            self.__position = value

    def __str__(self):
        """my_print Print the square.

        Returns:
            None.

        """
        x = self.__size
        pos = self.__position
        tmp = ""

        if x == 0:
            print()
            return tmp

        for k in range(pos[1]):
            tmp += '\n'

        for i in range(x):
            tmp += ' ' * pos[0]
            for j in range(x):
                tmp += '#'
            tmp += '\n'
        return tmp
