# simulate_traffic.py
import requests
import random

url = "http://127.0.0.1:8000/predict"

for _ in range(50):
    payload = {
        "MedInc": random.uniform(1, 15),
        "HouseAge": random.uniform(1, 50),
        "AveRooms": random.uniform(2, 10),
        "AveBedrms": random.uniform(0.8, 1.5),
        "Population": random.uniform(100, 3000),
        "AveOccup": random.uniform(1, 5),
        "Latitude": random.uniform(32, 42),
        "Longitude": random.uniform(-124, -114)
    }
    response = requests.post(url, json=payload)
    print(response.json())