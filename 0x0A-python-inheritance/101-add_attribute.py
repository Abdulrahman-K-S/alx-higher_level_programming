#!/usr/bin/python3
''' add_attribute function '''


def add_attribute(obj, name, value):
    '''add_attribute

    function that adds a new attribute
    to an object if it’s possible

    Attributes:
        obj (any): The attribute to add.
        name (str): The name of the attribute.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object can’t have new attribute.
    '''
    if isinstance(obj, (int, float, str, tuple, bool, dict, frozenset)):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
