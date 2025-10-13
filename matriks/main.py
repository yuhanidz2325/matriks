# matriks/main.py
from matrix import Matrix
from exporters.csv_exporter import export_to_csv
from exporters.json_exporter import export_to_json


if __name__ == "__main__":
    print("\n--- Menguji Matrix Exporters ---")

    # Buat objek matriks untuk demo
    matriks_demo = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    # Ekspor ke CSV
    print("Mengekspor matriks ke format CSV...")
    export_to_csv(matriks_demo, "matriks_output.csv")

    # Ekspor ke JSON
    print("\nMengekspor matriks ke format JSON...")
    export_to_json(matriks_demo, "matriks_output.json")



