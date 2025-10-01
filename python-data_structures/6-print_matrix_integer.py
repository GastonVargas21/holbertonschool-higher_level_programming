#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if not row:
            print()
            continue
        line = ""
        for num in row:
            line += "{:d} ".format(num)
        print(line.rstrip())
