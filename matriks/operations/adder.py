from matriks.matrix import Matrix

def add_matrices(matrix_a, matrix_b):
    if matrix_a.rows != matrix_b.rows or matrix_a.cols != matrix_b.cols:
        raise ValueError("Matriks harus memiliki ukuran yang sama untuk dijumlahkan")

    data = []
    for i in range(matrix_a.rows):
        row = []
        for j in range(matrix_a.cols):
            row.append(matrix_a.get_value(i, j) + matrix_b.get_value(i, j))
        data.append(row)

    return Matrix(data)  # ✅ cukup satu argumen

