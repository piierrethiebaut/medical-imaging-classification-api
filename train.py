"""
Script d'entraînement / fine-tuning reproductible du ResNet50 sur CheXpert-small.
Version "propre" de ce qui est exploré dans notebooks/01_exploration.ipynb.

Usage:
    python train.py --epochs 10 --batch-size 32
"""

# TODO:
#   - argparse pour les hyperparamètres
#   - device: torch.device("mps") si disponible, sinon "cpu"
#   - DataLoader sur CheXpert-small (train.csv / valid.csv)
#   - ResNet50 pré-entraîné (torchvision.models), fine-tuning dernière(s) couche(s)
#   - boucle d'entraînement + calcul métriques (accuracy, AUC par pathologie)
#   - sauvegarde du .pth final + push optionnel vers Hugging Face Hub
