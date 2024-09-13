#!/usr/bin/python3
"""
This module provides a function that adds two integers or floats.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats.
    
    Args:
        a: The first number, must be an integer or float.
        b: The second number, defaults to 98, must be an integer or float.
    
    Returns:
        The sum of a and b as an integer.
    
    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
