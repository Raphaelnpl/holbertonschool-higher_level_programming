#!/usr/bin/python3
'''Module of the class BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Return the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''Return a string that represents the rectangle description'''
        return f"[Rectangle] {self.__width}/{self.__height}"

