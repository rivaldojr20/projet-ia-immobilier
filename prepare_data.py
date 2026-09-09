# prepare_data.py
from sklearn.datasets import fetch_california_housing
import pandas as pd

# Chargement du dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Sauvegarde en CSV dans le dossier data/
df.to_csv("data/housing.csv", index=False)

print("Données sauvegardées avec succès !")
print(df.head())