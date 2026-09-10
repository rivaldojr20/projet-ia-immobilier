# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# 1. Initialisation de l'application
app = FastAPI(title="API Prédiction Prix Immobilier")

# 2. Chargement du modèle au démarrage du serveur
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# 3. Définition du format des données attendues (Validation automatique)
class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

# 4. Route d'accueil (pour vérifier que l'API tourne)
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction immobilière 🏠"}

# 5. Route de prédiction
@app.post("/predict")
def predict(features: HouseFeatures):
    # Transformation des données en tableau numpy
    input_data = np.array([[
        features.MedInc,
        features.HouseAge,
        features.AveRooms,
        features.AveBedrms,
        features.Population,
        features.AveOccup,
        features.Latitude,
        features.Longitude
    ]])
    
    # Prédiction
    prediction = model.predict(input_data)
    
    return {
        "prix_predit_en_centaines_de_milliers": round(float(prediction[0]), 2)
    }