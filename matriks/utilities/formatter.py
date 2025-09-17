def to_string(matrix):
    """Mengubah matriks menjadi string dengan format baris-kolom."""
    result = []
    for row in matrix.data:
        result.append(" ".join(map(str, row)))
    return "\n".join(result)  
