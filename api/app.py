from fastapi import FastAPI
from schemas import CustomerData
import sys
from pathlib import Path
import joblib

app = FastAPI(title="StreamFlix Churn Predictor")

@app.on_event('startup')
def load_model_on_startup():
    prod_model = joblib.load(f'{(Path(__file__).parent.parent)}/models/best_model.pkl')
    return prod_model

@app.get("/")
def health_check():
    return {"status": "healthy", "message": "API running"}
    pass




if __name__ == '__main__':
    print(f"Current WD {Path(__file__).parent.parent}")
    pass
    
