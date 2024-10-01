#!/usr/bin/python3
"""
Returns the dictionary description with simple data structure
for JSON serialization of an object.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure 
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        Dictionary with serializable attributes of the object.
    """
    return obj.__dict__
