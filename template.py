import os
from pathlib import Path

project_name = "StreamFlix_Churn_Analysis"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/data/raw/",
    f"{project_name}/data/processed/",  
    f"{project_name}/models/model.txt",
    f"{project_name}/notebooks/01_eda.ipynb",
    f"{project_name}/notebooks/02_preprocessing.ipynb",
    f"{project_name}/notebooks/03_modeling.ipynb",
    f"{project_name}/notebooks/04_evaluation.ipynb",

    f"{project_name}/src/data_preprocessing.py",
    f"{project_name}/src/feature_engineering.py",
    f"{project_name}/src/train.py",
    f"{project_name}/src/predict.py",

    f"{project_name}/api/app.py",
    f"{project_name}/api/schemas.py",


    f"{project_name}/monitoring/drift_detection.py",
    f"{project_name}/monitoring/performance_tracking.py",

    f"{project_name}/tests/test_preprocessing.py",
    f"{project_name}/tests/test_api.py",
    
    
    "Dockerfile",
    "requirements.txt",
    "config.yaml"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")