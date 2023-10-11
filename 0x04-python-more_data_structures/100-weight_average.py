#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 0

    numerator = sum(x[0] * x[1] for x in my_list)
    denumerator = sum(x[1] for x in my_list)
    return (numerator/denumerator)
