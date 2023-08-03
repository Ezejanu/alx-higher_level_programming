#!/usr/bin/python3
""" This function defines a class Node """

class Node:
""" This class defines a node of a singly linked list """

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value != None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        newNode = Node(value)

        if self.__head is None:
            newNode.next_node = None
            self.__head = newNode
        elif value < self.__head.data:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            newNode.next_node = temp.next_node
            temp.next_node = newNode

    def __str__(self):
        temp = self.__head
        while temp.next_node is not None:
            print("{}".format(temp.data))
            temp = temp.next_node
        print("{}".format(temp.data), end="")
        return ""


