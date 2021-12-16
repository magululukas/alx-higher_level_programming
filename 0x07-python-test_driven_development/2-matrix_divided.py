#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ a function that divides all elements of a matrix."""
    matrix = [
        [0, 1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6]
    ]
    div = round(matrix, 2)
    new_matrix = (matrix / div)
    return new_matrix
    if matrix != type([], int, float):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if div != type(int, float):
        raise TypeError('div must be a number')

