import numpy as np

def is_square(matrix):
    """
    Mengecek apakah matriks adalah matriks persegi (square matrix)
    
    Args:
        matrix: numpy array atau list 2D
        
    Returns:
        bool: True jika matriks persegi, False jika tidak
    """
    if isinstance(matrix, list):
        matrix = np.array(matrix)
    
    if matrix.ndim != 2:
        return False
    
    rows, cols = matrix.shape
    return rows == cols

def validate_square(matrix, operation_name="operasi"):
    """
    Validasi matriks persegi dengan error handling
    
    Args:
        matrix: numpy array atau list 2D
        operation_name: nama operasi untuk pesan error
        
    Raises:
        ValueError: jika matriks bukan persegi
    """
    if not is_square(matrix):
        shape = matrix.shape if hasattr(matrix, 'shape') else (len(matrix), len(matrix[0]))
        raise ValueError(
            f"Matriks harus persegi untuk {operation_name}. "
            f"Matriks yang diberikan memiliki dimensi {shape[0]}x{shape[1]}"
        )
    return True

if __name__ == "__main__":
    # Test
    square_matrix = [[1, 2], [3, 4]]
    non_square_matrix = [[1, 2, 3], [4, 5, 6]]
    
    print("Testing is_square:")
    print(f"Matriks 2x2: {is_square(square_matrix)}")  # True
    print(f"Matriks 2x3: {is_square(non_square_matrix)}")  # False

