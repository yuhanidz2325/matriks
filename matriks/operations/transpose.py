import numpy as np

class Transposer:
    """Kelas untuk melakukan operasi transpose matriks."""

    @staticmethod
    def transpose(matrix):
        """
        Mengembalikan transpose dari matriks input.
        """
        try:
            return np.transpose(matrix)
        except Exception as e:
            raise ValueError(f"Gagal melakukan transpose: {e}")
