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
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file

        Saves the instances of the objects in a file.

        Attributes:
            cls (obj): The class.
            list_objs (list): A list of object instances. Either a
                              list of Rectangle or Square classes.
        """
        filename = "{}.json".format(cls.__name__)
        list_attributes = []

        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            for elem in list_objs:
                list_attributes.append(elem.to_dictionary())
            return f.write(cls.to_json_string(list_attributes))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string

        Returns a list of the JSON string representation.

        Attributes:
            json_string (str): A string representation of a list of
                               dictionaries.

        Return:
            (list)
        """
        if json_string is None:
            return []
        return json.loads(json_string)
