from regression_model import run_regression
import pandas as pd

def save_results_to_csv(filename='results.csv'):
    results = run_regression()  # sekarang ini dictionary

    # Ambil perbandingan aktual vs prediksi
    comparison_df = pd.DataFrame(results.get('comparison', []))
    
    # Simpan perbandingan ke CSV
    comparison_df.to_csv(filename, index=False)
    print(f"Hasil regresi (comparison) disimpan ke '{filename}'")

    # Jika ada metrics (mis. {'mse':..., 'rmse':..., 'r2':...}), simpan terpisah
    metrics = results.get('metrics') or results.get('scores')
    if metrics:
        metrics_df = pd.DataFrame([metrics])  # satu baris dengan kolom mse, rmse, ...
        metrics_filename = filename.replace('.csv', '_metrics.csv')
        metrics_df.to_csv(metrics_filename, index=False)
        print(f"Metrics disimpan ke '{metrics_filename}'")

    # Alternatif: tambahkan metrics sebagai kolom berulang pada setiap baris comparison
    # if metrics and not comparison_df.empty:
    #     for k, v in metrics.items():
    #         comparison_df[k] = v
    #     comparison_df.to_csv(filename, index=False)
    #     print(f"Hasil regresi dan metrics disimpan ke '{filename}' (metrics ditambahkan sebagai kolom)")

if __name__ == "__main__":
    save_results_to_csv()

# from regression_model import run_regression
# import pandas as pd

# def save_results_to_csv(filename='results.csv'):
#     results = run_regression()  # sekarang ini dictionary

#     # Ambil perbandingan aktual vs prediksi
#     comparison_df = pd.DataFrame(results['comparison'])
    
#     # Simpan ke CSV
#     comparison_df.to_csv(filename, index=False)
#     print(f"Hasil regresi disimpan ke '{filename}'")

# if __name__ == "__main__":
#     save_results_to_csv()

# from regression_model import run_regression
# import pandas as pd

# def save_results_to_csv(filename='results.csv'):
#     results = run_regression()  # sekarang ini dictionary

#     # Ambil perbandingan aktual vs prediksi
#     comparison_df = pd.DataFrame(results['comparison'])
    
#     # Simpan ke CSV
#     comparison_df.to_csv(filename, index=False)
#     print(f"Hasil regresi disimpan ke '{filename}'")

# if __name__ == "__main__":
#     save_results_to_csv()