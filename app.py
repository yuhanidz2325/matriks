from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # Baca comparison (actual vs prediction) dari results.csv
    try:
        df_results = pd.read_csv('results.csv')
    except Exception as e:
        print(f"Error reading results.csv: {e}")
        df_results = pd.DataFrame()
    
    # Baca metrics dari results_metrics.csv (MSE, RMSE, R2_Score)
    try:
        df_metrics = pd.read_csv('results_metrics.csv')
    except Exception as e:
        print(f"Error reading results_metrics.csv: {e}")
        df_metrics = pd.DataFrame()
    
    # HTML tabel untuk ditampilkan di web
    results_table_html = df_results.head(50).to_html(
        classes='table table-striped table-hover', 
        index=False
    ) if not df_results.empty else "<p class='text-warning'>File results.csv tidak ditemukan</p>"
    
    metrics_table_html = df_metrics.to_html(
        classes='table table-striped table-bordered', 
        index=False
    ) if not df_metrics.empty else "<p class='text-warning'>File results_metrics.csv tidak ditemukan</p>"
    
    # Data sebagai list of dict untuk JS / Chart.js
    comparison_data = df_results.to_dict(orient='records') if not df_results.empty else []
    metrics_data = df_metrics.to_dict(orient='records') if not df_metrics.empty else []
    
    # Extract individual metrics untuk ditampilkan di cards
    metrics_values = {}
    if not df_metrics.empty:
        row = df_metrics.iloc[0]  # Ambil baris pertama
        metrics_values = {
            'mse': float(row.get('MSE', 0)),
            'rmse': float(row.get('RMSE', 0)),
            'r2_score': float(row.get('R2_Score', 0))
        }
    
    # Kirim semua data ke template
    return render_template('index.html',
                           results_table=results_table_html,
                           comparison_data=comparison_data,
                           metrics_table=metrics_table_html,
                           metrics_data=metrics_data,
                           metrics_values=metrics_values)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)