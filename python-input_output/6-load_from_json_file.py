#!/usr/bin/python3
"""Module that defines load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file

    Args:
        filename: name of the JSON file to read from

    Returns:
        Python object created from the JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
