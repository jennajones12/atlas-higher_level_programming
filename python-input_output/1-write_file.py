#!/usr/bin/python3
"""
defines write function
"""


def write_file(filename="", text=""):
    """
    writes string to text file and returns number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as file:
        chars = file.write(text)
        return (chars)
