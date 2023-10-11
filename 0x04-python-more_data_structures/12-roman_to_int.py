#!/usr/bin/python3

def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return None

    roman_values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
    result = 0
    prev_value = 0

    for c in roman_string[::-1]:
        current_value = roman_values[c]
        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value
        prev_value = current_value

    return result
