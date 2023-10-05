#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if sys.argv[2] != '+' and sys.argv[2] != '-':
            if sys.argv[2] != '*' and sys.argv[2] != '/':
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)

        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            operation = add
        elif sys.argv[2] == '-':
            operation = sub
        elif sys.argv[2] == '*':
            operation = mul
        else:
            operation = div

        print("{} {} {}".format(a, op, b), end=" = ")
        print("{}".format(operation(a, b)))
