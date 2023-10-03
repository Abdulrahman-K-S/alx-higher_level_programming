#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is".format(number), end=" ")

if number >= 0:
    last_digit = number % 10
    print(last_digit, end=" ")
else:
    last_digit = (number * -1) % 10 * -1
    print(last_digit, end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
elif last_digit < 6:
    print("and is less than 6 and not 0")
