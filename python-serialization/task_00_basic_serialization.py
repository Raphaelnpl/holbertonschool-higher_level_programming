#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize the given Python dictionary and save it to the specified JSON file.
    
    Args:
        data (dict): A Python dictionary to be serialized.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified JSON file to recreate the Python dictionary.
    
    Args:
        filename (str): The filename of the input JSON file.
        
    Returns:
        dict: A Python dictionary with the deserialized JSON data.
    """
    with open(filename, 'r') as json_file:
        return json.load(json_file)
