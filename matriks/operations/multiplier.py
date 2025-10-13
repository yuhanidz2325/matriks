# matriks/operations/multiplier.py

def multiply_matrices(matrix_a, matrix_b):
    """Mengalikan dua matriks dengan cara dasar (O(n^3))"""
    if matrix_a.cols != matrix_b.rows:
        raise ValueError("Jumlah kolom matriks A harus sama dengan jumlah baris matriks B.")

    result_data = []
    for i in range(matrix_a.rows):
        row = []
        for j in range(matrix_b.cols):
            total = 0
            for k in range(matrix_a.cols):
                total += matrix_a.data[i][k] * matrix_b.data[k][j]
            row.append(total)
        result_data.append(row)

    # Gunakan kelas Matrix supaya tetap konsisten
    from matriks.matrix import Matrix
    return Matrix(result_data)

