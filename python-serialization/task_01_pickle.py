#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.
        
        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted string.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to the specified file using pickle.
        
        Args:
            filename (str): The name of the file where the object will be serialized.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from the specified file using pickle.
        
        Args:
            filename (str): The name of the file where the object is stored.
            
        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error deserializing object: {e}")
            return None
