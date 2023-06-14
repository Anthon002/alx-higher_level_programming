#!/usr/bin/python3
def square_matrix_comprehension(matrix=[]):
    sqrd_mtrx = [[elem**2 for elem in i] for i in matrix]
    return (sqrd_mtrx)
