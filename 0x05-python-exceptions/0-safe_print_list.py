#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0

    try:
        for i in my_list:
            if idx < x:
                print("{:d}".format(my_list[idx]), end='')
                idx += 1
    except TypeError:
        pass

    print()
    return idx
