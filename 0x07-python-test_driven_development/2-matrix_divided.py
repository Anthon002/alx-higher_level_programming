#!/usr/bin/python3
"""
    This module is for the division of matrices
"""
def matrix_divided(matrix, div):
    """
    This function Divides matrix elements by div

    Args:
        matrix: The Matrix
        div(int/float): The dividing number

    Returns:
        matrix_2: a matrix

    Raise:
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0
        TypeError: if matrix size is not the same
        TypeError: if matrix element is not a number

    """
    matrix_2 = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]

    if (type(div) != int and type(div) != float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if (matrix ==[]):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for j in (range(len(matrix[i]))):
                if type(matrix[i][j]) != int and type (matrix[i][j] != float):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                matrix_2[i][j] = round((matrix[i][j] /div),2)
    return (matrix_2)
