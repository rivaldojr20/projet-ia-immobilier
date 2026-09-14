# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
from datetime import datetime
import os

app = FastAPI(title="API Prédiction Prix Immobilier")

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction immobilière"}

@app.post("/predict")
def predict(features: HouseFeatures):
    input_data = np.array([[
        features.MedInc, features.HouseAge, features.AveRooms,
        features.AveBedrms, features.Population, features.AveOccup,
        features.Latitude, features.Longitude
    ]])

    prediction = model.predict(input_data)
    result = round(float(prediction[0]), 2)

    #  LOG : on enregistre la requête + la prédiction pour le monitoring
    log_entry = features.model_dump()
    log_entry["prediction"] = result
    log_entry["timestamp"] = datetime.now().isoformat()

    log_df = pd.DataFrame([log_entry])
    log_file = "logs/production_data.csv"
    os.makedirs("logs", exist_ok=True)

    if os.path.exists(log_file):
        log_df.to_csv(log_file, mode="a", header=False, index=False)
    else:
        log_df.to_csv(log_file, mode="w", header=True, index=False)

    return {"prix_predit_en_centaines_de_milliers": result}