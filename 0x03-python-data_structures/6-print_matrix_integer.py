#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for n in range(len(matrix[x])):
            print("{:d}".format(matrix[x][n]))
            if n != (len(matrix[x]) - 1):
                print(" ", end="")

