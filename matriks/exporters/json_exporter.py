# matriks/exporters/json_exporter.py

def export_to_json(matrix, filename):
    """
    Fungsi untuk mengekspor matriks ke file JSON
    1. Ubah data matrix menjadi list of lists
    2. Konversi ke string JSON
    3. Simpan ke file 'filename'
    4. Tampilkan pesan sukses
    """
    import json
    with open(filename, mode="w") as file:
        json.dump(matrix.data, file, indent=4)
    print(f"✅ Matriks berhasil diekspor ke {filename}")
