#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    is_key = a_dictionary.keys()

    for k in is_key:
        if k == key:
            a_dictionary[key] = value
            return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
