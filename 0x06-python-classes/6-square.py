#!/usr/bin/python3
class Square:
    def __init__(self, __size=0, __position=(0, 0)):
        self.size = __size
        self.position = __position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
            return
        elif value < 0:
            raise ValueError('size must be >= 0')
            return
        else:
            self.__size = value

    def my_print(self):
        x = self.__size
        pos = self.__position

        if x == 0:
            print()

        for k in range(pos[1]):
            print()

        for i in range(x):
            print(' ' * pos[0], end='')
            for j in range(x):
                print('#', end='')
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):

        if type(value) != tuple and value != None:
            raise TypeError('position must be a tuple of 2 positive integers')
            return
        if len(value) != 2:
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
