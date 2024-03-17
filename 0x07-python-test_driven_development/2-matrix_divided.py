#!/usr/bin/python3

""" Python function that divides all element of a matirx"""


def matrix_divided(matrix, div):
    """ divides each value in the matrix by div and retuns new matrix """

    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    lenofmatrix = len(matrix)
    for i in matrix:
        for items in i:
            if not isinstance(items, (int, float)):
                raise TypeError(error)
    len_of_first = len(matrix[0])
    for i in matrix:
        if len(i) != len_of_first:
            raise TypeError("Each row of the matrix must have the same size")

    sum = []
    for i in matrix:
        mul = [round(x/div, 2) for x in i]
        sum.append(mul)

    return sum
