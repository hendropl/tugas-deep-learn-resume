#webinar 1 Patterns of Data with Analysis and AI
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Studi Kasus: Analisis Diagnostik & Prediktif Invoice (Late Payment)
def main():
    print("=== Prediksi Keterlambatan Pembayaran Invoice ===")
    
    # 1. Data Preparation (Memakan 80-90% waktu analisis di dunia nyata)
    # Membuat dataset dummy representing data perusahaan
    data = {
        'invoice_amount': [1500, 2500, 500, 8000, 1200, 6000],
        'customer_tenure_months': [12, 24, 2, 60, 5, 36],
        'is_late_payment': [0, 0, 1, 0, 1, 0] # Target: 1 (Telat), 0 (Tepat waktu)
    }
    df = pd.DataFrame(data)
    
    X = df[['invoice_amount', 'customer_tenure_months']]
    y = df['is_late_payment']
    
    # 2. Split data uji dan data latih
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Modeling menggunakan algoritma klasifikasi (Random Forest)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Evaluasi Model
    predictions = model.predict(X_test)
    print("\nHasil Klasifikasi:")
    print(f"Akurasi: {accuracy_score(y_test, predictions) * 100}%")
    print("Laporan Evaluasi:\n", classification_report(y_test, predictions, zero_division=0))

if __name__ == '__main__':
    main()