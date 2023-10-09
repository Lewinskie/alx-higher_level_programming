#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for item in my_string:
        if item != 'c' and item != 'C':
            string += item
    return string
