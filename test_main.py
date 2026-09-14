# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    """Vérifie que la route d'accueil répond correctement"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur l'API de prédiction immobilière"}

def test_predict():
    """Vérifie que la prédiction fonctionne et renvoie un nombre positif"""
    payload = {
        "MedInc": 8.3,
        "HouseAge": 41,
        "AveRooms": 6.9,
        "AveBedrms": 1.02,
        "Population": 322,
        "AveOccup": 2.55,
        "Latitude": 37.88,
        "Longitude": -122.23
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "prix_predit_en_centaines_de_milliers" in data
    assert data["prix_predit_en_centaines_de_milliers"] > 0

def test_predict_invalid_data():
    """Vérifie que l'API rejette des données invalides (ex: texte au lieu de nombre)"""
    payload = {
        "MedInc": "pas_un_nombre",
        "HouseAge": 41,
        "AveRooms": 6.9,
        "AveBedrms": 1.02,
        "Population": 322,
        "AveOccup": 2.55,
        "Latitude": 37.88,
        "Longitude": -122.23
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  # Erreur de validation attendue