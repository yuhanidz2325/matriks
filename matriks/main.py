from .matrix import Matrix
from .exporters.csv_exporter import export_to_csv

def demo():
    matrix_c = Matrix([[10, 20], [30, 40]])
    print("\\nMenyimpan Matriks C ke file CSV:")
    export_to_csv(matrix_c, "matriks_c.csv")

if __name__ == "__main__":
    demo()
