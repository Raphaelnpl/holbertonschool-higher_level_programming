#!/usr/bin/python3

"""this function returns True if \
the object is a class \
that inherited (directly or indirectly)"""


def inherits_from(obj, a_class):
    """this method returns True if \class \
that inherited (directly or indirectly)"""

    return isinstance(obj, a_class) and type(obj) is not a_class