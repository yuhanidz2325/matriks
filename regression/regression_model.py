import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def run_regression():
    # 1. Baca dataset
    df = pd.read_csv('insurance_encoded.csv')  # Pastikan path benar

    # 2. Pilih variabel independen dan dependen
    X = df[['age', 'bmi', 'children', 'smoker_yes',
            'region_northwest', 'region_southeast', 'region_southwest']]
    y = df['charges']

    # 3. Split data menjadi data latih dan data uji (80%:20%)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 4. Bangun model regresi linier
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 5. Prediksi data uji
    y_pred = model.predict(X_test)

    # 6. Evaluasi model
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    # 7. Buat dictionary hasil agar bisa dibaca Flask
    result = {
        "intercept": float(model.intercept_),
        "coefficients": {col: float(coef) for col, coef in zip(X.columns, model.coef_)},
        "metrics": {
            "MSE": float(mse),
            "RMSE": float(rmse),
            "R2_Score": float(r2)
        },
        "comparison": pd.DataFrame({
            "Actual": y_test,
            "Predicted": y_pred
        }).head(10).to_dict(orient="records")
    }

    return result