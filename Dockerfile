# 1. Image de base légère avec Python déjà installé
FROM python:3.10-slim

# 2. Définir le dossier de travail à l'intérieur du conteneur
WORKDIR /app

# 3. Copier uniquement le fichier des dépendances d'abord
#    (Astuce de performance : Docker met en cache cette étape si le fichier ne change pas)
COPY requirements.txt .

# 4. Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier tout le reste du code source dans le conteneur
COPY . .

# 6. Exposer le port utilisé par l'API
EXPOSE 8000

# 7. Commande de démarrage du serveur au lancement du conteneur
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]