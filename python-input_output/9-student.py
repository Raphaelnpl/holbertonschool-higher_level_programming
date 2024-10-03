#!/usr/bin/python3
class Student:
    """A class that defines a student by first name, last name, and age"""
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
