#!/usr/bin/python3
'''A module that defines a Student class.'''

class Student:
    """A class that defines a student by first name, last name, and age."""
    
    def __init__(self, first_name, last_name, age):
        """Initializes the student attributes."""
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

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.
        Assumes json will always be a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)

if __name__ == "__main__":
    student = Student("John", "Doe", 23)
    print(student.to_json())

    data = {"first_name": "Jane", "last_name": "Doe", "age": 24}
    student.reload_from_json(data)
    print(student.to_json())
