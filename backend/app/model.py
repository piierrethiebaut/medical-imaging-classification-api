"""
Chargement du modèle ResNet50 fine-tuné (poids téléchargés depuis Hugging Face Hub)
et fonctions d'inférence.
"""

# TODO:
#   - télécharger les poids via huggingface_hub.hf_hub_download (HF_MODEL_REPO)
#   - charger l'architecture ResNet50 (torchvision) + state_dict
#   - device: MPS en local, CPU sur Render (pas de GPU sur Render free tier)
#   - fonction predict(image) -> (label, confidence)
