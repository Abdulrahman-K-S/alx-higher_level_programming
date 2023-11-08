#!/usr/bin/python3
'''A module that reads the inputed file'''


def read_file(filename=""):
    ''' function that reads a text file (UTF8) and prints it to stdout '''
    with open(filename, encoding='utf-8') as f:
        read_file = f.read()
    print('{:s}'.format(read_file), end='')
