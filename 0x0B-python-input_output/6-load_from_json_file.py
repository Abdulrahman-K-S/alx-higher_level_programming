#!/usr/bin/python3
'''
A module that creates an Object from a “JSON file”.
'''


import json


def load_from_json_file(filename):
    '''load_from_json_file

    Creates an object from a "JSON file".

    Return:
       (obj): The objected created.
    '''
    with open(filename, mode='r') as f:
        return json.load(f)
