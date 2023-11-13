#!/usr/bin/python3
"""Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees
    clockwise.
    Args:
        matrix (list): matrix, list of list
    """
    tmp = []
    size = len(matrix)
    for i in range(size):
        tmp.append([])
        for j in range(size):
            tmp[i].append(matrix[size - j - 1][i])
    matrix[:] = list(tmp)
