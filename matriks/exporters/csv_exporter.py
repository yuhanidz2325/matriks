# matriks/exporters/csv_exporter.py

def export_to_csv(matrix, filename):
    """
    Fungsi untuk mengekspor matriks ke file CSV
    1. Buka file dengan nama 'filename' dalam mode tulis
    2. Buat objek writer CSV
    3. Tuliskan setiap baris data dari matrix ke dalam file
    4. Tampilkan pesan sukses
    """
    import csv
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in matrix.data:
            writer.writerow(row)
    print(f"✅ Matriks berhasil diekspor ke {filename}")
