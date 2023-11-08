#!/usr/bin/python3
'''
A module that returns the JSON representation of an object (string).
'''


import json


def to_json_string(my_obj):
    '''to_json_string

    function that returns the JSON representation of an object.

    Return:
        (str): The JSON representation of an object.
    '''
    return json.dumps(my_obj)
