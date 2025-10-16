import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import os

def run_regression():
    # 1. Baca dataset
    df = pd.read_csv('insurance_encoded.csv')  # ubah path sesuai lokasi file kamu

    # 2. Pilih variabel independen dan dependen
    X = df[['age', 'bmi', 'children', 'smoker_yes', 'region_northwest', 'region_southeast', 'region_southwest']]
    y = df['charges']

    # 3. Split data menjadi data latih dan data uji (80%:20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Bangun model regresi linier
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 5. Prediksi data uji
    y_pred = model.predict(X_test)

    # 6. Evaluasi model
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print("=== HASIL REGRESI LINIER ===")
    print(f"Intercept: {model.intercept_}")
    print("Koefisien masing-masing variabel:")
    for col, coef in zip(X.columns, model.coef_):
            print(f"  {col}: {coef:.4f}")

    print("\n=== EVALUASI MODEL ===")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
    print(f"R² Score: {r2:.4f}")

    # 7. Contoh perbandingan aktual vs prediksi
    compare = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print("\nPerbandingan nilai aktual vs prediksi:")
    print(compare.head())