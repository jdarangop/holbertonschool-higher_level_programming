#!/usr/bin/python3


class Node:
    """Node for the linked list.

    Attributes:
        data (int): Data.
        next_node (Node): Next node.

    """

    def __init__(self, data, next_node=None):
        """__init__ function.

        Args:
            data: The first parameter.
            next_node: The second parameter.

        Returns:
            None.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data function.

        Returns:
            self.__data.

        """
        return self.__data

    @data.setter
    def data(self, value):
        """data setter function.

        Args:
            value: value for data atributte..

        Returns:
            None.

        """
        if type(data) != int:
            raise TypeError('data must be an integer')
        else:
            self.__data = data

    @property
    def next_node(self):
        """next_node property function.

        Returns:
            self.__next_node

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter function.

        Args:
            value: Value for the first node of the list.

        Returns:
            None.

        """
        if next_node is not None and type(next_node) != Node:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = next_node


class SinglyLinkedList:
    """Singly linked list.

    Attributes:
        head (Node): Head of the linked list.

    """
    def __init__(self):
        """__init__ function.

        Returns:
            None.

        """
        self.__head = None

    def sorted_insert(self, value):
        """__init__ function.

        Args:
            data: The first parameter.
            next_node: The second parameter.

        Returns:
            None.

        """
        head = self.__head

        #if head is None:
        new_node = Node(value, head)
        self.__head = new_node
