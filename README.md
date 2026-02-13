## 📊 Problem Statement

StreamFlix, a subscription-based streaming service, is experiencing a 15% monthly churn rate, costing $750,000 per month. This project builds a production ML system to predict which customers will cancel next month, enabling proactive retention strategies.

## 🎯 Business Impact

- **Current Churn:** 15% monthly (1,500 customers)
- **Cost per Lost Customer:** $500 lifetime value
- **Target:** Reduce churn by 30% through targeted interventions
- **Potential Savings:** $225,000/month

## 📁 Project Structure
```
StreamFlix_Churn_Analysis/
├── data/
│   ├── raw/              # Original datasets
│   └── processed/        # Cleaned, preprocessed data
├── notebooks/
│   ├── 01_eda.ipynb     # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb
│   ├── 03_modeling_validation.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train.py
│   └── predict.py
├── api/
│   ├── app.py           # FastAPI endpoints
│   └── schemas.py       # Request/response models
├── monitoring/
│   ├── drift_detection.py
│   └── performance_tracking.py
├── tests/
│   ├── test_preprocessing.py
│   └── test_api.py
└── requirements.txt
```

## 🚀 Quick Start

### Installation
```bash
# Clone repository
git clone https://github.com/aakashascend-cell/StreamFlix_Churn_Analysis.git
cd StreamFlix_Churn_Analysis

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

**1. Data Preprocessing**
```bash
python src/data_preprocessing.py
```

**2. Train Model**
```bash
python src/train.py
```

**3. Run API**
```bash
uvicorn api.app:app --reload
```

**4. Make Predictions**
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d @sample_customer.json
```