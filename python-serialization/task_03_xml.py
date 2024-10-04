#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format and save it to the specified file.
    
    Args:
        dictionary (dict): The dictionary to be serialized.
        filename (str): The name of the XML file where data will be saved.
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    with open(filename, 'wb') as xml_file:
        tree.write(xml_file)

def deserialize_from_xml(filename):
    """
    Deserialize data from an XML file into a Python dictionary.
    
    Args:
        filename (str): The name of the XML file to be deserialized.
    
    Returns:
        dict: The deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text
        
        return deserialized_dict
    
    except (FileNotFoundError, ET.ParseError) as e:
        print(f"Error deserializing XML: {e}")
        return None
