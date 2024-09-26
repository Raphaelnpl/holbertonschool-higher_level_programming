#!/usr/bin/python3
'''
Module containing the function is_kind_of_class
'''

def is_kind_of_class(obj, a_class):
    '''Returns True if obj is an instance of a_class or a subclass, False otherwise'''
    return isinstance(obj, a_class)
