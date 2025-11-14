import numpy as np

def add(A, B):
    """
    Penjumlahan matriks secara manual (A + B)
    
    Syarat: A dan B harus memiliki dimensi yang sama
    
    Args:
        A: numpy array
        B: numpy array dengan dimensi sama dengan A
        
    Returns:
        numpy array: hasil penjumlahan A + B
        
    Raises:
        ValueError: jika dimensi tidak sama
    """
    if isinstance(A, list):
        A = np.array(A)
    if isinstance(B, list):
        B = np.array(B)
    
    # Validasi dimensi
    if A.shape != B.shape:
        raise ValueError(
            f"Dimensi tidak sama untuk penjumlahan matriks. "
            f"A: {A.shape}, B: {B.shape}"
        )
    
    # Buat matriks hasil dengan dimensi yang sama
    result = np.zeros_like(A, dtype=float)
    
    # Penjumlahan elemen per elemen
    if A.ndim == 1:
        # Untuk vektor 1D
        for i in range(len(A)):
            result[i] = A[i] + B[i]
    else:
        # Untuk matriks 2D
        m, n = A.shape
        for i in range(m):
            for j in range(n):
                result[i, j] = A[i, j] + B[i, j]
    
    return result

def add_scalar(matrix, scalar):
    """
    Menambahkan scalar ke setiap elemen matriks
    
    Args:
        matrix: numpy array
        scalar: angka yang akan ditambahkan
        
    Returns:
        numpy array: setiap elemen ditambah dengan scalar
    """
    if isinstance(matrix, list):
        matrix = np.array(matrix)
    
    result = np.zeros_like(matrix, dtype=float)
    
    if matrix.ndim == 1:
        for i in range(len(matrix)):
            result[i] = matrix[i] + scalar
    else:
        m, n = matrix.shape
        for i in range(m):
            for j in range(n):
                result[i, j] = matrix[i, j] + scalar
    
    return result

if __name__ == "__main__":
    # Test penjumlahan matriks
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    B = np.array([[7, 8, 9],
                  [10, 11, 12]])
    
    print("Matriks A:")
    print(A)
    
    print("\nMatriks B:")
    print(B)
    
    print("\nA + B:")
    result = add(A, B)
    print(result)
    
    print("\nVerifikasi dengan numpy +:")
    print(A + B)
    print(f"Hasil sama: {np.allclose(result, A + B)}")
    
    # Test penjumlahan scalar
    print("\n" + "="*40)
    print("Test penjumlahan scalar:")
    C = np.array([[1, 2], [3, 4]])
    scalar = 10
    print(f"\nMatriks C:\n{C}")
    print(f"\nC + {scalar}:")
    print(add_scalar(C, scalar))