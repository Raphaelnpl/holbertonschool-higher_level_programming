#!/usr/bin/python3
"""
Module to generate Pascal's triangle.
"""

def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = []
    
    for i in range(n):
        row = [None for _ in range(i + 1)]
        row[0], row[-1] = 1, 1

        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

if __name__ == "__main__":
    print(pascal_triangle(5))
