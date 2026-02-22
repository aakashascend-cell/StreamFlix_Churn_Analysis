import joblib
from pathlib import Path
import pandas as pd

def load_model():
    prod_model = joblib.load(f"{Path(__file__).parent.parent}/models/best_model.pkl")
    return prod_model

def predict_churn(prod_model,customer_data):
    """Predict if customer will churn"""
    prediction = prod_model.predict(customer_data)[0]
    probability = prod_model.predict_proba(customer_data)[0][1]

    if prediction == 1:
        prediction_category = "Yes"
    else:
        prediction_category = "No"
    
    return prediction_category, probability

if __name__ == "__main__":
    
    customer = {
        'gender': 'Male',
        'SeniorCitizen': 'No',
        'Partner': 'Yes',
        'Dependents': 'No',
        'tenure': 12,
        'PhoneService': 'Yes',
        'MultipleLines': 'No',
        'InternetService': 'Fiber optic',
        'OnlineSecurity': 'No',
        'OnlineBackup': 'Yes',
        'DeviceProtection': 'No',
        'TechSupport': 'No',
        'StreamingTV': 'Yes',
        'StreamingMovies': 'No',
        'Contract': 'Month-to-month',
        'PaperlessBilling': 'Yes',
        'PaymentMethod': 'Electronic check',
        'MonthlyCharges': 70.35,
        'TotalCharges': 844.2
    }

    prod_model = load_model()

    prediction_category, probability = predict_churn(prod_model,pd.DataFrame([customer]))
    

    print(f"Will this customer get churned?: {prediction_category}")
    print(f"What is the probability of churn: {probability:.2%}")