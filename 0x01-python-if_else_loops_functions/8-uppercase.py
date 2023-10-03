#!/usr/bin/python3
def uppercase(string):
    for character in string:
        if 97 <= ord(character) <= 122:
            character = chr(ord(character) - 32)
        print("{}".format(character), end="")
    print()
