#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """

    for i in range(int(len(matrix) / 2)):
        for j in range(i, (len(matrix) - i - 1)):
            x = (len(matrix) - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[(len(matrix) - i - 1)][x]
            matrix[(len(matrix) - i - 1)][x] = matrix[j][(len(matrix) - i - 1)]
            matrix[j][(len(matrix) - i - 1)] = tmp

