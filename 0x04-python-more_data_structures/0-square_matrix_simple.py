#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    if matrix == []:
        return []

    new_matrix = []
    for elem in matrix[:]:
        new_matrix.append(list(map(lambda x: x ** 2, elem)))

    return new_matrix
