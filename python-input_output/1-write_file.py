#!/usr/bin/python3
"""Module that defines write_file function"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return number of characters

    Args:
        filename: name of the file to write to
        text: text to write to the file

    Returns:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
