#!/usr/bin/python3
"""
function to append a string to a text file
"""

def append_write(filename="", text=""):
    """
    Appends str at end of text file and returns num of chars added

    Args:
        filename (str): name of file to append to
        text (str): string to append to file

    Returns:
        int: number of chars added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
