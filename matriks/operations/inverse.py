import numpy as np
from matriks.validators.is_square import is_square

class Inverser:
    """Kelas untuk menghitung inverse matriks."""

    @staticmethod
    def inverse(matrix):
        """
        Mengembalikan inverse dari matriks persegi.
        """
        if not is_square(matrix):
            raise ValueError("Matriks harus persegi untuk dihitung inversenya.")

        try:
            return np.linalg.inv(matrix)
        except np.linalg.LinAlgError:
            raise ValueError("Matriks tidak memiliki inverse (singular).")
