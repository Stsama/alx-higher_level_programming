#!/usr/bin/python3
# 0-square_matrix_simple.py
# Ezoula Albert
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    return ([list(map(lambda x: x * x, rows) for rows in matrix)])
