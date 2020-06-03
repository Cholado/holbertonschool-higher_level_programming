#!/usr/bin/python3
"""
Module - "pascal_triangle" function
"""

def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    ret = [[1]]

    for i in range(1, n):
        row = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                res = ret[i-1][j-1]+ret[i-1][j]
                row.append(res)

        ret.append(row)
    return ret
