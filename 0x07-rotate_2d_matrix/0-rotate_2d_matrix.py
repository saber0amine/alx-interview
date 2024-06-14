#!/usr/bin/python3
"""file that contains the function"""


def rotate_2d_matrix(matrix):
    """rotate a 2D matrix"""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
