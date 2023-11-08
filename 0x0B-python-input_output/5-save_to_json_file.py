#!/usr/bin/python3
'''
A module that writes an Object to a text file, using a JSON representation.
'''


import json


def save_to_json_file(my_obj, filename):
    '''save_to_json_file

    Writes an Object to a text file, using a JSON representation.
    '''
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
