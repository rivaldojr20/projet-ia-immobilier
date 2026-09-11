# train.py
import pandas as pd
import mlflow
import mlflow.sklearn
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Chargement des données
print("Chargement des données...")
df = pd.read_csv("data/housing.csv")

X = df.drop("MedHouseVal", axis=1)  # Toutes les colonnes sauf le prix
y = df["MedHouseVal"]               # La cible : le prix médian de la maison

# 2. Split Train / Test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Démarrage du suivi MLflow
mlflow.set_experiment("prediction_prix_immobilier")

with mlflow.start_run():
    
    # Hyperparamètres du modèle
    n_estimators = 100
    max_depth = 10
    
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    
    # 4. Entraînement du modèle
    print("Entraînement du modèle en cours...")
    model = RandomForestRegressor(
        n_estimators=n_estimators, 
        max_depth=max_depth, 
        random_state=42
    )
    model.fit(X_train, y_train)
    
    # 5. Évaluation
    predictions = model.predict(X_test)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)
    
    print(f"RMSE: {rmse}")
    print(f"R2 Score: {r2}")
    
    # Enregistrement des métriques dans MLflow
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2_score", r2)
    
    # 6. Sauvegarde du modèle dans MLflow
    mlflow.sklearn.log_model(model, "random_forest_model")
    
    # 7. Export du modèle en fichier .pkl (pour l'étape 2 - FastAPI)
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)
    
    print("Modèle sauvegardé dans models/model.pkl")