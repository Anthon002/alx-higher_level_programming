#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_sqrd = [matrix[i] for i in range(len(matrix))]
    for i in range(0, len(matrix_sqrd)):
        for j in range(0, len(matrix_sqrd[i])):
            matrix_sqrd[i][j] *= matrix_sqrd[i][j]
    return(matrix_sqrd)
