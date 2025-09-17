def is_square(matrix):
    return all(len(row) == len(matrix[0]) for row in matrix)
