import numpy as np

def transpose(matrix):
    """
    Menghitung transpose dari matriks secara manual
    Transpose: menukar baris menjadi kolom dan kolom menjadi baris
    
    Args:
        matrix: numpy array 2D dengan dimensi (m, n)
        
    Returns:
        numpy array: matriks transpose dengan dimensi (n, m)
        
    Example:
        Input:  [[1, 2, 3],
                 [4, 5, 6]]
        Output: [[1, 4],
                 [2, 5],
                 [3, 6]]
    """
    if isinstance(matrix, list):
        matrix = np.array(matrix)
    
    m, n = matrix.shape  # m baris, n kolom
    
    # Buat matriks kosong untuk hasil transpose (n x m)
    result = np.zeros((n, m))
    
    # Tukar baris dan kolom
    for i in range(m):
        for j in range(n):
            result[j, i] = matrix[i, j]
    
    return result

if __name__ == "__main__":
    # Test
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    print("Matriks A:")
    print(A)
    print(f"Dimensi: {A.shape}")
    
    print("\nTranspose A:")
    At = transpose(A)
    print(At)
    print(f"Dimensi: {At.shape}")
    
    # Verifikasi dengan numpy
    print("\nVerifikasi dengan numpy.T:")
    print(A.T)
    print(f"Hasil sama: {np.allclose(At, A.T)}")
