def is_square(matrix):
    # Cek apakah matriks tidak kosong dan memiliki panjang baris sama
    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        return False
    # Cek apakah jumlah baris == jumlah kolom
    return len(matrix) == len(matrix[0])

