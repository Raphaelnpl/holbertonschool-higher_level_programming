#!/usr/bin/python3
'''
Module containing the function inherits_from
'''

def inherits_from(obj, a_class):
    '''
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from the specified class, False otherwise.
    '''
    return isinstance(obj, a_class) and type(obj) is not a_class
touch 