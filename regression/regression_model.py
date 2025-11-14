import pandas as pd
import numpy as np
import sys
import os

# Import modul dari folder matriks
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from matriks.operations.multiplier import multiply
from matriks.operations.transpose import transpose
from matriks.operations.inverse import inverse
from matriks.operations.adder import add
from matriks.operations.subtractor import subtract

def train_test_split_manual(X, y, test_size=0.2, random_state=42):
    """Split data secara manual"""
    np.random.seed(random_state)
    n = len(X)
    indices = np.arange(n)
    np.random.shuffle(indices)
    
    test_count = int(n * test_size)
    test_indices = indices[:test_count]
    train_indices = indices[test_count:]
    
    X_train = X[train_indices]
    X_test = X[test_indices]
    y_train = y[train_indices]
    y_test = y[test_indices]
    
    return X_train, X_test, y_train, y_test

def fit_linear_regression(X, y):
    """
    Hitung koefisien regresi linear secara manual menggunakan modul matriks
    Menggunakan formula: β = (X^T X)^(-1) X^T y
    """
    # Tambahkan kolom intercept (kolom 1)
    ones = np.ones((len(X), 1))
    X_with_intercept = np.column_stack([ones, X])
    
    # Hitung X^T menggunakan modul transpose
    Xt = transpose(X_with_intercept)
    
    # Hitung X^T × X menggunakan modul multiplier
    XtX = multiply(Xt, X_with_intercept)
    
    # Hitung (X^T X)^(-1) menggunakan modul inverse
    XtX_inv = inverse(XtX)
    
    # Hitung X^T × y
    y_reshaped = y.reshape(-1, 1)
    Xty = multiply(Xt, y_reshaped)
    
    # Hitung β = (X^T X)^(-1) × X^T y
    beta = multiply(XtX_inv, Xty)
    beta = beta.flatten()
    
    intercept = beta[0]
    coefficients = beta[1:]
    
    return intercept, coefficients

def predict(X, intercept, coefficients):
    """Prediksi menggunakan model"""
    # Prediksi manual: y = intercept + X · coefficients
    predictions = np.zeros(len(X))
    
    for i in range(len(X)):
        predictions[i] = intercept
        for j in range(len(coefficients)):
            predictions[i] += X[i, j] * coefficients[j]
    
    return predictions

def mean_squared_error_manual(y_true, y_pred):
    """Hitung MSE secara manual"""
    n = len(y_true)
    
    # Hitung error menggunakan modul subtractor
    errors = subtract(y_true.reshape(-1, 1), y_pred.reshape(-1, 1)).flatten()
    
    # Kuadratkan error
    squared_errors = errors ** 2
    
    # Rata-rata
    mse = np.sum(squared_errors) / n
    return mse

def r2_score_manual(y_true, y_pred):
    """Hitung R² score secara manual"""
    # SS_res = Σ(y_true - y_pred)²
    residuals = subtract(y_true.reshape(-1, 1), y_pred.reshape(-1, 1)).flatten()
    ss_res = np.sum(residuals ** 2)
    
    # SS_tot = Σ(y_true - mean(y_true))²
    y_mean = np.mean(y_true)
    total_deviation = y_true - y_mean
    ss_tot = np.sum(total_deviation ** 2)
    
    # R² = 1 - (SS_res / SS_tot)
    r2 = 1 - (ss_res / ss_tot)
    return r2

def run_regression():
    # 1. Baca dataset
    df = pd.read_csv('insurance_encoded.csv')
    
    # 2. Pilih variabel independen dan dependen
    feature_cols = ['age', 'bmi', 'children', 'smoker_yes',
                    'region_northwest', 'region_southeast', 'region_southwest']
    X = df[feature_cols].values.astype(np.float64)
    y = df['charges'].values.astype(np.float64)
    
    # 3. Split data secara manual (80%:20%)
    X_train, X_test, y_train, y_test = train_test_split_manual(
        X, y, test_size=0.2, random_state=42
    )
    
    # 4. Bangun model regresi linier dengan modul matriks
    print("Menghitung koefisien regresi menggunakan modul matriks...")
    intercept, coefficients = fit_linear_regression(X_train, y_train)
    
    # 5. Prediksi data uji
    y_pred = predict(X_test, intercept, coefficients)
    
    # 6. Evaluasi model
    mse = mean_squared_error_manual(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score_manual(y_test, y_pred)
    
    # 7. Buat dictionary hasil
    result = {
        "intercept": float(intercept),
        "coefficients": {col: float(coef) for col, coef in zip(feature_cols, coefficients)},
        "metrics": {
            "MSE": float(mse),
            "RMSE": float(rmse),
            "R2_Score": float(r2)
        },
        "comparison": [
            {"Actual": float(actual), "Predicted": float(pred)}
            for actual, pred in zip(y_test[:10], y_pred[:10])
        ]
    }
    
    return result

# Contoh penggunaan
if __name__ == "__main__":
    print("="*60)
    print("REGRESI LINEAR MENGGUNAKAN MODUL MATRIKS CUSTOM")
    print("="*60)
    
    result = run_regression()
    
    print(f"\nIntercept: {result['intercept']:.2f}")
    print("\nKoefisien:")
    for feature, coef in result['coefficients'].items():
        print(f"  {feature}: {coef:.4f}")
    
    print("\nMetrik Evaluasi:")
    print(f"  MSE: {result['metrics']['MSE']:.2f}")
    print(f"  RMSE: {result['metrics']['RMSE']:.2f}")
    print(f"  R² Score: {result['metrics']['R2_Score']:.4f}")
    
    print("\nPerbandingan 10 Data Pertama:")
    print(f"{'Actual':>12} {'Predicted':>12} {'Error':>12}")
    print("-"*40)
    for item in result['comparison']:
        error = item['Actual'] - item['Predicted']
        print(f"{item['Actual']:>12.2f} {item['Predicted']:>12.2f} {error:>12.2f}")