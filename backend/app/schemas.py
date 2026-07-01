"""
Schémas Pydantic pour les requêtes/réponses de l'API.
"""

from pydantic import BaseModel


class PredictionResponse(BaseModel):
    label: str
    confidence: float
    heatmap_base64: str | None = None


# TODO: affiner selon la sortie multi-label de CheXpert (14 pathologies)
#   -> probablement list[PredictionResponse] ou dict[str, float]
