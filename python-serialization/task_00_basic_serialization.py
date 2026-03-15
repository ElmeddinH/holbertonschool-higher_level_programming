#!/usr/bin/env python3
"""Module for basic serialization and deserialization"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize and save data to a JSON file

    Args:
        data: Python dictionary with data
        filename: name of the output JSON file
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file

    Args:
        filename: name of the input JSON file

    Returns:
        Python dictionary with deserialized JSON data
    """
    with open(filename, 'r') as f:
        return json.load(f)
