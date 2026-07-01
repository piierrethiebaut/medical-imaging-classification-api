"""
Point d'entrée de l'API FastAPI.
Définit les routes : health check, upload + inférence.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Medical Imaging Classification API",
    description="API de classification de radiographies thoraciques (CheXpert) avec explicabilité GradCAM.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    """Vérifie que l'API est en ligne."""
    return {"status": "ok"}


# TODO: endpoint POST /predict
#   - upload d'une image
#   - preprocessing (preprocessing.py)
#   - inférence (model.py)
#   - génération heatmap GradCAM (gradcam.py)
#   - retour: prédiction + confiance + heatmap encodée
