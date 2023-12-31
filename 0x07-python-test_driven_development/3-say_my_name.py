#!/usr/bin/python3
"""
Modue say_my_name
say_my_name
"""
def say_my_name(first_name, last_name=""):
    """
    Prints a persons full name
    """
    if type(first_name) != str:
        raise TypeError('First_name must be a string')
    if type(last_name) != str:
        raise TypeError('Last_name must be a string')
    print("My name is " + first_name + " " + last_name)
