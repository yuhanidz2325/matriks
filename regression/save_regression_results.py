from regression_model import run_regression
import pandas as pd

def save_results_to_csv(filename='results.csv'):
    """
    Menyimpan hasil regresi ke file CSV
    Membuat 3 file:
    1. results_comparison.csv - Perbandingan Actual vs Predicted
    2. results_metrics.csv - Metrik evaluasi (MSE, RMSE, R²)
    3. results_coefficients.csv - Intercept dan Koefisien
    """
    # Jalankan regresi dan dapatkan hasil
    results = run_regression()
    
    # 1. Simpan perbandingan Actual vs Predicted
    comparison_df = pd.DataFrame(results['comparison'])
    comparison_filename = filename.replace('.csv', '_comparison.csv')
    comparison_df.to_csv(comparison_filename, index=False)
    print(f"✓ Perbandingan Actual vs Predicted disimpan ke '{comparison_filename}'")
    
    # 2. Simpan metrics (MSE, RMSE, R²)
    metrics = results['metrics']
    metrics_df = pd.DataFrame([metrics])
    metrics_filename = filename.replace('.csv', '_metrics.csv')
    metrics_df.to_csv(metrics_filename, index=False)
    print(f"✓ Metrics (MSE, RMSE, R²) disimpan ke '{metrics_filename}'")
    
    # 3. Simpan koefisien dan intercept
    coefficients = results['coefficients']
    coef_data = [
        {'Feature': 'Intercept', 'Coefficient': results['intercept']}
    ]
    for feature, coef in coefficients.items():
        coef_data.append({'Feature': feature, 'Coefficient': coef})
    
    coef_df = pd.DataFrame(coef_data)
    coef_filename = filename.replace('.csv', '_coefficients.csv')
    coef_df.to_csv(coef_filename, index=False)
    print(f"✓ Koefisien model disimpan ke '{coef_filename}'")
    
    # 4. (Opsional) Buat ringkasan lengkap dalam satu file
    print("\n" + "="*60)
    print("RINGKASAN HASIL REGRESI")
    print("="*60)
    print(f"\nIntercept: {results['intercept']:.4f}")
    print("\nKoefisien:")
    for feature, coef in coefficients.items():
        print(f"  {feature}: {coef:.4f}")
    print("\nMetrik Evaluasi:")
    for metric, value in metrics.items():
        print(f"  {metric}: {value:.4f}")
    print("\n" + "="*60)

def save_full_predictions(filename='full_predictions.csv'):
    """
    (Opsional) Menyimpan semua prediksi, bukan hanya 10 data pertama
    Catatan: Perlu modifikasi di regression_model.py untuk return semua data
    """
    results = run_regression()
    comparison_df = pd.DataFrame(results['comparison'])
    comparison_df.to_csv(filename, index=False)
    print(f"✓ Semua prediksi disimpan ke '{filename}'")

if __name__ == "__main__":
    # Simpan hasil regresi
    save_results_to_csv('results.csv')
    
    # Uncomment jika ingin menyimpan semua prediksi
    # save_full_predictions('full_predictions.csv')