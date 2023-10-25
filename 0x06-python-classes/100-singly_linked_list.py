# #!/usr/bin/python3
"""100-singly_linked_list.py"""


class Node:
    """Class Node

    This class defines a node to be places in a singly linked list.

    Attributes:
        data (int): The data of the node.
        next_node (class <node>): A pointer to the next node.
    """

    __data = None
    __next_node = None

    def __init__(self, data, next_node=None):
        """__init__

        The class Node's constructor

        Args:
            data (int): The data for the node.
            next_node (class <Node>): The pointer to the next node.

        Raises:
            TypeError: If the data is not an int.
            TypeError: If the node is not of type class <Node>.
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        """data setter

        This functions sets the data attribute.

        Args;
            data (int): The data to be placed in the node.

        Raises:
            TypeError: If the data type is not of type int.
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """next_node setter

        This functions sets the next_node attribute.

        Args;
            next_node (class <node>): A pointer to the next node.

        Raises:
            TypeError: If the next_node type is not of type class <node>.
        """
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """class SinglyLinkedList"""

    __head = None

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return

        current_node = self.__head
        while (current_node.next_node):
            current_node = current_node.next_node

        current_node.next = new_node

    def __repr__(self):
        current_node = self.__head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next_node
