#!/usr/bin/python3
'''
Function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class; otherwise False
'''



def inherits_from(obj, a_class):
    '''
    Arguments:
        @obj (any): object to evaluate
        @a_class (any): class instance
    Return:
        `True` if the object is an instance of a class that inherited,
        otherwise `False`
    '''
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True

    return False
