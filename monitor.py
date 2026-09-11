# monitor.py
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset, DataSummaryPreset
from evidently.legacy.test_suite import TestSuite
from evidently.legacy.test_preset import DataDriftTestPreset

# 1. Données de référence (celles utilisées pour l'entraînement)
reference_data = pd.read_csv("data/housing.csv")
reference_data = reference_data.drop("MedHouseVal", axis=1)  # on garde que les features

# 2. Données actuelles (celles reçues en production via l'API)
current_data = pd.read_csv("logs/production_data.csv")
current_data = current_data.drop(["prediction", "timestamp"], axis=1)  # on garde les mêmes colonnes

# 3. Création du rapport Evidently
report = Report(metrics=[
    DataDriftPreset(),
    DataSummaryPreset(),
])

snapshot = report.run(reference_data=reference_data, current_data=current_data)

# 4. Sauvegarde du rapport en HTML
snapshot.save_html("logs/data_drift_report.html")

print(" Rapport de monitoring généré : logs/data_drift_report.html")
# monitor.py (ajout à la fin du fichier)


# Test automatisé avec seuil d'alerte
tests = TestSuite(tests=[DataDriftTestPreset()])
tests.run(reference_data=reference_data, current_data=current_data)

# Résultat sous forme de dictionnaire (facile à automatiser)
result = tests.as_dict()
drift_detected = result["summary"]["failed_tests"] > 0

if drift_detected:
    print(" ALERTE : Data Drift détecté ! Il faut ré-entraîner le modèle (retour à l'Étape 1).")
else:
    print(" Tout va bien, pas de dérive significative des données.")