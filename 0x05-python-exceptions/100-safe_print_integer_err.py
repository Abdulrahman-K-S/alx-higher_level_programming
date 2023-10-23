#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as valerr:
        sys.stderr.write("Exception: " + str(valerr) + "\n")
        return False
    except TypeError as typerr:
        sys.stderr.write("Exception: " + str(typerr) + "\n")
        return False
