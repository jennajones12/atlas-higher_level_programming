#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in str:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:
            result += chr(ascii_val - 32)
        else:
            result += char
            print(result)
            print()
