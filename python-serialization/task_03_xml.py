#!/usr/bin/env python3
"""Module for serializing and deserializing with XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML and save to a file

    Args:
        dictionary: Python dictionary to serialize
        filename: name of the XML file to save to
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize XML file to a Python dictionary

    Args:
        filename: name of the XML file to read from

    Returns:
        Python dictionary with deserialized data
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
