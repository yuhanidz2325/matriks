# matriks/matrix.py
class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)              # jumlah baris
        self.cols = len(data[0]) if data else 0  # jumlah kolom

    def get_value(self, row, col):
        """Mengambil nilai pada baris dan kolom tertentu"""
        return self.data[row][col]

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.data)
