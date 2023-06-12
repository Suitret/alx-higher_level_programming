#!/usr/bin/python3
"""Module which contains Node class
   and SinglyLinkedList class
"""


class Node:
    """class Node that defines
       a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """function that initializes attributes
        Args:
            self : the object
            data (int): the data
            next_node : the next node
        Returns:
            void
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        self.__data = data

        if not isinstance(next_node, Node) and next_node != None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = next_node

    @property
    def data(self):
        """function that returns the data
        Args:
            self : the object
        Returns:
            the data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """function that sets the data
        Args:
            self : the object
            value (int): the value
        Returns:
            void
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """function that returns the next node
        Args:
            self : the object
        Returns:
            the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """function that sets the next node
        Args:
            self : the object
            value (int): the value
        Returns:
            void
        """
        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """class SinglyLinkedList that defines a SinglyLinkedList"""

    def __init__(self):
        """function that initializes attributes
        Args:
            self : the object
        Returns:
            void
        """
        self.__head = None

    def sorted_insert(self, value):
        """function that inserts node in the list
        Args:
            self : the object
            value (int): the value
        Returns:
            void
        """
        if not isinstance(value, int):
            return

        if not self.__head:
            new = Node(value)
            self.__head = new
        else:
            temp = self.__head

            while temp and temp.data < value:
                temp = temp.next_node

            new = Node(value, temp)

            if temp == self.__head:
                self.__head = new
            else:
                temp = self.__head
                while temp.next_node and temp.next_node.data < value:
                    temp = temp.next_node
                temp.next_node = new

    def __str__(self):
        """function that returns a list in str format
        Args:
            self : the object
        Returns:
            string
        """
        res = ""
        hd = self.__head

        if not hd:
            return res
        else:
            while hd:
                res += str(hd.data)
                if hd.next_node:
                    res += '\n'
                hd = hd.next_node
            return res
