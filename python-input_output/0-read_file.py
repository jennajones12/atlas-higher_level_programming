#!/usr/bin/python3
"""
provides function to read and print a text file
"""

def read_file(filename=""):
    """
    Reads text file and prints to stdout

    Args:
        filename (str): name of ile to read
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
