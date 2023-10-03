#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_digit = number % 10
    else:
        last_digit = (number * -1) % 10 * -1

    return last_digit
