#!/usr/bin/python3
try:
    raise_exception_msg("This is a custom error message.")
except NameError as e:
    print(e)
