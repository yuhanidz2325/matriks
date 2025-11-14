import numpy as np

def multiply(A, B):
    """
    Perkalian matriks secara manual (A × B)
    
    Syarat: Jumlah kolom A harus sama dengan jumlah baris B
    Hasil: Matriks dengan dimensi (baris A, kolom B)
    
    Args:
        A: numpy array dengan dimensi (m, n)
        B: numpy array dengan dimensi (n, p)
        
    Returns:
        numpy array: hasil perkalian dengan dimensi (m, p)
        
    Raises:
        ValueError: jika dimensi tidak kompatibel
    """
    if isinstance(A, list):
        A = np.array(A)
    if isinstance(B, list):
        B = np.array(B)
    
    # Validasi dimensi
    if A.ndim == 1:
        A = A.reshape(-1, 1)
    if B.ndim == 1:
        B = B.reshape(-1, 1)
    
    m, n = A.shape  # A: m x n
    n2, p = B.shape  # B: n x p
    
    if n != n2:
        raise ValueError(
            f"Dimensi tidak kompatibel untuk perkalian matriks. "
            f"A: {A.shape}, B: {B.shape}. "
            f"Jumlah kolom A ({n}) harus sama dengan jumlah baris B ({n2})"
        )
    
    # Buat matriks hasil (m x p)
    result = np.zeros((m, p))
    
    # Perkalian matriks manual
    for i in range(m):
        for j in range(p):
            # Hitung dot product dari baris i di A dengan kolom j di B
            for k in range(n):
                result[i, j] += A[i, k] * B[k, j]
    
    return result

def multiply_scalar(matrix, scalar):
    """
    Perkalian matriks dengan skalar
    
    Args:
        matrix: numpy array
        scalar: angka
        
    Returns:
        numpy array: setiap elemen dikalikan dengan scalar
    """
    if isinstance(matrix, list):
        matrix = np.array(matrix)
    
    result = np.zeros_like(matrix, dtype=float)
    
    if matrix.ndim == 1:
        for i in range(len(matrix)):
            result[i] = matrix[i] * scalar
    else:
        m, n = matrix.shape
        for i in range(m):
            for j in range(n):
                result[i, j] = matrix[i, j] * scalar
    
    return result

if __name__ == "__main__":
    # Test perkalian matriks
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])  # 2x3
    
    B = np.array([[7, 8],
                  [9, 10],
                  [11, 12]])  # 3x2
    
    print("Matriks A (2x3):")
    print(A)
    
    print("\nMatriks B (3x2):")
    print(B)
    
    print("\nA × B (hasil 2x2):")
    result = multiply(A, B)
    print(result)
    
    print("\nVerifikasi dengan numpy @ operator:")
    print(A @ B)
    print(f"Hasil sama: {np.allclose(result, A @ B)}")
    
    # Test perkalian scalar
    print("\n" + "="*40)
    print("Test perkalian scalar:")
    C = np.array([[1, 2], [3, 4]])
    scalar = 3
    print(f"\nMatriks C:\n{C}")
    print(f"\nC × {scalar}:")
    print(multiply_scalar(C, scalar))