#!/usr/bin/python3
'''class json'''

class Student:
    """A class that defines a student by first name, last name, and age"""
    
    def __init__(self, first_name, last_name, age):
        """Initializes the student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes contained in this list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for key in attrs:
            if key in self.__dict__:
                new_dict[key] = self.__dict__[key]
        return new_dict

if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    print(student_1.to_json())
    print(student_2.to_json(['first_name', 'age']))

    