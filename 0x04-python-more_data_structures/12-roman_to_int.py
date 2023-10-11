#!/usr/bin/python3

def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return None

    roman_int = 0
    for i in roman_string:
        if i == "I":
            roman_int += 1
        elif roman_string[i] == "V" and roman_string[i - 1] == "I":
            roman_int += 5 - 2
        elif roman_string[i] == "V":
            roman_int += 5
        elif roman_string[i] == "X" and roman_string[i - 1] == "I":
            roman_int += 10 - 2
        elif i == "L":
            roman_int += 50
        elif i == "C":
            roman_int += 100
        elif i == "D":
            roman_int += 500
        elif i == "M":
            roman_int += 1000

    return roman_int
