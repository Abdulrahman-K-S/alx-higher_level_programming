#!/usr/bin/python3
'''
Module to over-write the content of the files and
return the number of lines overwritten.
'''


def number_of_lines(filename=""):
    ''' function that returns the number of lines of a text file '''
    with open(filename) as f:
        i = 0
        for line in enumerate(f):
            i += 1
    return i
