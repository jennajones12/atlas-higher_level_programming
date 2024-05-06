#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arguments = argv[1:]

    total = 0

    for arg in arguments:
        total += int(arg)

        print(total)
