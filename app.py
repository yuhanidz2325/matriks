from flask import Flask, render_template
import pandas as pd
import sys
import os

# Tambahkan path untuk import regression_model
sys.path.append(os.path.join(os.path.dirname(__file__), 'regression'))

app = Flask(__name__)

@app.route('/')
def home():
    """Route utama - menampilkan dashboard hasil regresi"""
    # ... kode kamu yang sudah ada ...
    
    try:
        df_results = pd.read_csv('results_comparison.csv')
        print(f"✅ Berhasil membaca results_comparison.csv ({len(df_results)} baris)")
    except FileNotFoundError:
        print("⚠️  File results_comparison.csv tidak ditemukan")
        df_results = pd.DataFrame()
    except Exception as e:
        print(f"❌ Error reading results_comparison.csv: {e}")
        df_results = pd.DataFrame()
    
    try:
        df_metrics = pd.read_csv('results_metrics.csv')
        print(f"✅ Berhasil membaca results_metrics.csv")
    except FileNotFoundError:
        print("⚠️  File results_metrics.csv tidak ditemukan")
        df_metrics = pd.DataFrame()
    except Exception as e:
        print(f"❌ Error reading results_metrics.csv: {e}")
        df_metrics = pd.DataFrame()
    
    results_table_html = df_results.head(50).to_html(
        classes='table table-striped table-hover', 
        index=False,
        border=0
    ) if not df_results.empty else "<p class='text-warning'>⚠️ File results_comparison.csv tidak ditemukan.</p>"
    
    metrics_table_html = df_metrics.to_html(
        classes='table table-striped table-bordered', 
        index=False,
        border=0
    ) if not df_metrics.empty else "<p class='text-warning'>⚠️ File results_metrics.csv tidak ditemukan.</p>"
    
    comparison_data = df_results.to_dict(orient='records') if not df_results.empty else []
    metrics_data = df_metrics.to_dict(orient='records') if not df_metrics.empty else []
    
    metrics_values = {}
    if not df_metrics.empty:
        row = df_metrics.iloc[0]
        metrics_values = {
            'mse': float(row.get('MSE', 0)),
            'rmse': float(row.get('RMSE', 0)),
            'r2_score': float(row.get('R2_Score', 0))
        }
    else:
        metrics_values = {
            'mse': 0,
            'rmse': 0,
            'r2_score': 0
        }
    
    return render_template('index.html',
                           results_table=results_table_html,
                           comparison_data=comparison_data,
                           metrics_table=metrics_table_html,
                           metrics_data=metrics_data,
                           metrics_values=metrics_values)

# ========== TAMBAHKAN INI! ==========
@app.route('/health')
def health_check():
    """
    Health check endpoint untuk Docker
    """
    return {
        'status': 'healthy',
        'message': 'Application is running',
        'port': 8000
    }, 200

@app.route('/generate')
def generate_csv():
    """
    Route untuk generate file CSV hasil regresi
    """
    try:
        from regression.save_regression_results import save_results_to_csv
        save_results_to_csv()
        return {
            'status': 'success',
            'message': 'File CSV berhasil di-generate!',
            'files': [
                'results_comparison.csv',
                'results_metrics.csv',
                'results_coefficients.csv'
            ]
        }, 200
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Error generating CSV: {str(e)}'
        }, 500
# =====================================

if __name__ == "__main__":
    print("=" * 70)
    print("🚀 Starting Flask Application - Regresi Linear Project")
    print("=" * 70)
    
    csv_files = ['results_comparison.csv', 'results_metrics.csv']
    missing_files = [f for f in csv_files if not os.path.exists(f)]
    
    if missing_files:
        print("\n⚠️  WARNING: File CSV belum ada!")
        print(f"   Missing: {', '.join(missing_files)}")
        print("\n📝 Silakan jalankan command berikut terlebih dahulu:")
        print("   python regression/save_regression_results.py")
        print("\n💡 Atau akses: http://localhost:8000/generate")
    else:
        print("\n✅ Semua file CSV tersedia")
    
    print("\n" + "=" * 70)
    print("📊 Server berjalan di:")
    print("   - Local:    http://localhost:8000")
    print("   - Network:  http://0.0.0.0:8000")
    print("   - Health:   http://localhost:8000/health")
    print("   - Generate: http://localhost:8000/generate")
    print("=" * 70)
    print("\n⌨️  Tekan CTRL+C untuk menghentikan server\n")
    
    app.run(host="0.0.0.0", port=8000, debug=True)