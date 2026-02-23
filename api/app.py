from fastapi import FastAPI
from .schemas import CustomerData
import sys
from pathlib import Path
import joblib
import pandas as pd

model = None  # Global
app = FastAPI(title="StreamFlix Churn Predictor")

@app.on_event('startup')
def load_model_on_startup():
    global model
    model = joblib.load(f"{(Path(__file__).parent.parent)}/models/best_model.pkl")
    

@app.get("/")
def health_check():
    return {"status": "healthy", "message": "API running"}
    

@app.post("/predict")
def predict_churn_endpoint(customer: CustomerData):
    customer_dict = customer.model_dump()
    customer_df = pd.DataFrame([customer_dict])
    result = model.predict(customer_df)
    return {"prediction": int(result[0])}

if __name__ == '__main__':
    model = load_model_on_startup()
    
    
