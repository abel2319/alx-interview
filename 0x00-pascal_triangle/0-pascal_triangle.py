#!/usr/bin/python3
"""
pascal triangle module
"""


def pascal_triangle(n):
    """
    Return the triangle
    """
    pascal_triangle = []
    if n > 0:
        if n == 1:
            return [[1]]
        elif n == 2:
            return [[1], [1, 1]]
        else:
            row = [1, 1]
            tmp = []
            pascal_triangle = [[1], [1, 1]]
            for i in range(2, n):
                tmp.append(1)
                j = 0
                for j in range(1, i):
                    tmp.append(row[j-1] + row[j])
                tmp.append(1)
                pascal_triangle.append(tmp)
                row = tmp
                tmp = []
    return pascal_triangle
