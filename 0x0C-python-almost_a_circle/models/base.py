#!/usr/bin/python3
"""Base Module"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string

        Returns a representation of the `list_dictionaries` in JSON
        format.

        Attributes:
            list_dictionaries (list): A dictionary in a list.

        Return:
            (str): The JSON string representation of `list_dictionaries` if
                   its not None otherwise []
        """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
