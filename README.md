# Prédiction du Prix de l'Immobilier — Pipeline MLOps

> Projet de fin d'année réalisé par :
>
> - **496 H-TOL — TOGNENDRAZA Ravalomanana Francis Bien Aimé**
> - **424 H-TOL — AVOFANEVAMIRATRINIANA Jocaya Elsevline**
> - **502 H-TOL — VAHIA Jean Christian Rivaldo**
> - Formation : **IG Toliara**

Ce projet illustre la mise en place d'un **pipeline MLOps complet**, allant de l'entraînement d'un modèle de Machine Learning jusqu'à son déploiement en production et sa surveillance continue.

🔗 **API en ligne (déployée) :** [https://prediction-immobilier-api.onrender.com/docs](https://prediction-immobilier-api.onrender.com/docs)

> ⚠️ Le service gratuit Render peut mettre 30 à 60 secondes à se "réveiller" au premier appel après une période d'inactivité.

---

## Objectif du projet

Prédire le prix médian d'une maison en Californie à partir de 8 caractéristiques (revenu du quartier, âge du bâtiment, nombre de pièces, localisation géographique, etc.), en suivant les bonnes pratiques **MLOps** utilisées en entreprise.

---

## Architecture du pipeline

```

┌─────────────┐     ┌──────────┐     ┌────────────┐     ┌────────┐     ┌────────┐     ┌────────────┐
│ Entraînement│ --> │   Code   │ --> │   CI/CD    │ --> │ Build  │ --> │ Deploy │ --> │  Monitor   │
│ DVC/MLflow  │     │ FastAPI  │     │  GitHub    │     │ Docker │     │ Render │     │ Evidently  │
│ Scikit-learn│     │          │     │  Actions   │     │        │     │        │     │    AI      │
└─────────────┘     └──────────┘     └────────────┘     └────────┘     └────────┘     └──────┬─────┘
▲                                                                                     │
└─────────────────────────────── Feedback loop (data drift) ────────────────────────┘
```
