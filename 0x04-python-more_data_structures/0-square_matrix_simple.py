#!/usr/bin/python3
# 0-square_matrix_simple.py
# Ezoula Albert
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    new_matrix = []
    for rows in matrix:
        row = []
        for columns in rows:
            row.append(columns ** 2)
        new_matrix.append(row)
    return new_matrix
