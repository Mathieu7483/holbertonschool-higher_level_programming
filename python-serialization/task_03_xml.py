#!/usr/bin/python3
"""Module that using serialization and
deserialization using XML as an alternative to JSON"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to XML format"""
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize XML file to Python dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
