#!/usr/bin/python3
"""Base Module"""


class Base():
    """class Base
    
    Attributes:
        __nb_objects (int): An incrementer of how many instances
                            there is.
        id (int): The id of the class. If not assigned then
                  the number of instances.
    """
    __nb_objects = 0
    id = None

    def __init__(self, id=None):
        """class Base constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
