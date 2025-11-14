import numpy as np
import sys
import os

# Import validator
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from validators.is_square import validate_square

def inverse(matrix):
    """
    Menghitung inverse matriks menggunakan metode Gauss-Jordan Elimination
    
    Syarat: Matriks harus persegi dan non-singular (determinan != 0)
    
    Args:
        matrix: numpy array persegi (n x n)
        
    Returns:
        numpy array: matriks inverse
        
    Raises:
        ValueError: jika matriks tidak persegi atau singular
    """
    if isinstance(matrix, list):
        matrix = np.array(matrix, dtype=float)
    else:
        matrix = matrix.astype(float)
    
    # Validasi matriks persegi
    validate_square(matrix, "inverse")
    
    n = matrix.shape[0]
    
    # Buat matriks augmented [A | I]
    augmented = np.zeros((n, 2 * n))
    augmented[:, :n] = matrix.copy()
    augmented[:, n:] = np.eye(n)
    
    # Gauss-Jordan Elimination
    for i in range(n):
        # Cari pivot (elemen terbesar di kolom i)
        max_row = i
        for k in range(i + 1, n):
            if abs(augmented[k, i]) > abs(augmented[max_row, i]):
                max_row = k
        
        # Tukar baris jika perlu
        if max_row != i:
            augmented[[i, max_row]] = augmented[[max_row, i]]
        
        # Cek jika matriks singular
        if abs(augmented[i, i]) < 1e-10:
            raise ValueError(
                "Matriks singular (tidak memiliki inverse). "
                "Determinan mendekati nol."
            )
        
        # Normalisasi baris pivot
        pivot = augmented[i, i]
        augmented[i] = augmented[i] / pivot
        
        # Eliminasi kolom i di baris lain
        for j in range(n):
            if j != i:
                factor = augmented[j, i]
                augmented[j] = augmented[j] - factor * augmented[i]
    
    # Ambil bagian kanan sebagai inverse
    inverse_matrix = augmented[:, n:]
    
    return inverse_matrix

def determinant(matrix):
    """
    Menghitung determinan matriks secara rekursif
    
    Args:
        matrix: numpy array persegi
        
    Returns:
        float: nilai determinan
    """
    if isinstance(matrix, list):
        matrix = np.array(matrix, dtype=float)
    else:
        matrix = matrix.astype(float)
    
    validate_square(matrix, "determinan")
    
    n = matrix.shape[0]
    
    # Base case: matriks 1x1
    if n == 1:
        return matrix[0, 0]
    
    # Base case: matriks 2x2
    if n == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    
    # Ekspansi kofaktor sepanjang baris pertama
    det = 0
    for j in range(n):
        # Buat minor matrix (hapus baris 0 dan kolom j)
        minor = np.delete(np.delete(matrix, 0, axis=0), j, axis=1)
        # Kofaktor dengan tanda bergantian
        cofactor = ((-1) ** j) * matrix[0, j] * determinant(minor)
        det += cofactor
    
    return det

if __name__ == "__main__":
    # Test inverse matriks 2x2
    print("Test 1: Matriks 2x2")
    A = np.array([[4, 7],
                  [2, 6]], dtype=float)
    
    print("Matriks A:")
    print(A)
    
    print("\nInverse A:")
    A_inv = inverse(A)
    print(A_inv)
    
    print("\nVerifikasi A × A⁻¹ = I:")
    identity = A @ A_inv
    print(identity)
    print(f"Hasil = Identity: {np.allclose(identity, np.eye(2))}")
    
    # Test inverse matriks 3x3
    print("\n" + "="*50)
    print("Test 2: Matriks 3x3")
    B = np.array([[1, 2, 3],
                  [0, 1, 4],
                  [5, 6, 0]], dtype=float)
    
    print("Matriks B:")
    print(B)
    
    print("\nInverse B:")
    B_inv = inverse(B)
    print(B_inv)
    
    print("\nVerifikasi dengan numpy.linalg.inv:")
    B_inv_numpy = np.linalg.inv(B)
    print(B_inv_numpy)
    print(f"Hasil sama: {np.allclose(B_inv, B_inv_numpy)}")
    
    # Test determinan
    print("\n" + "="*50)
    print("Test Determinan:")
    print(f"det(A) = {determinant(A)}")
    print(f"det(B) = {determinant(B)}")