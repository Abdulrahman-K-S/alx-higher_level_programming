#!/usr/bin/python3
def remove_char_at(str, n):
    nstr = ""
    for i in range(len(str)):
        if i != n:
            nstr = nstr + str[i]
        continue

    return nstr
