#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_value = 0
    for x in range(len(roman_string)):
        if x > 0 and roman_dictionary[roman_string[x]] > roman_dictionary[roman_string[x - 1]]:
            int_value += roman_dictionary[roman_string[x]] - 2 * roman_dictionary[roman_string[x - 1]]
        else:
            int_value += roman_dictionary[roman_string[x]]
    return int_value
