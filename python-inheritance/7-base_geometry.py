#!/usr/bin/python3
'''
Module containing the class BaseGeometry
'''

class BaseGeometry:
    '''BaseGeometry class'''

    def area(self):
        '''
        Public instance method that raises an Exception
        with the message "area() is not implemented"
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Public instance method that validates 'value'

        Args:
            name (str): name of the value (always a string)
            value (int): the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
