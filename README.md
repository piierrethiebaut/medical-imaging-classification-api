# Medical Imaging Classification API

Classification de radiographies thoraciques (dataset **CheXpert-small**, Stanford ML Group) avec une API construite from scratch — pas de service tiers consommé — incluant une couche d'explicabilité via **GradCAM**.

Projet portfolio réalisé dans le cadre d'une recherche d'emploi en health tech (US), post-IFSBM.

> ⚠️ Projet à visée démonstrative / portfolio uniquement. Aucune utilisation clinique ou diagnostique.

## Architecture

```
┌─────────────┐      HTTP       ┌──────────────┐      inference       ┌────────────────┐
│  Streamlit  │ ───────────────▶│   FastAPI    │ ────────────────────▶│  ResNet50 +     │
│  Frontend   │◀─────────────── │   Backend    │◀──────────────────── │  GradCAM        │
└─────────────┘   prediction    └──────────────┘    label + heatmap   └────────────────┘
                                        │
                                        ▼
                              poids hébergés sur
                              Hugging Face Hub
```

- **Backend** : FastAPI + PyTorch (ResNet50 pré-entraîné, fine-tuné sur CheXpert-small) + GradCAM pour l'explicabilité
- **Frontend** : Streamlit — upload d'image, affichage de la prédiction, confiance, heatmap
- **Dataset** : [CheXpert-small](https://stanfordmlgroup.github.io/competitions/chexpert/) (11 GB, Stanford ML Group)
- **Poids du modèle** : hébergés sur Hugging Face Hub, téléchargés au démarrage de l'API
- **Déploiement** : Render (backend, via Dockerfile) + Streamlit Cloud (frontend)

## Structure du repo

```
medical-imaging-classification-api/
├── backend/            # API FastAPI
│   ├── app/
│   │   ├── main.py             # routes
│   │   ├── model.py            # chargement modèle + inférence
│   │   ├── preprocessing.py    # transformation des images
│   │   ├── gradcam.py          # heatmaps GradCAM
│   │   └── schemas.py          # modèles Pydantic
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/            # App Streamlit
│   ├── app.py
│   └── requirements.txt
├── notebooks/           # Exploration du dataset et prototypage
├── train.py             # Script d'entraînement reproductible
├── models/              # (vide, gitignored — poids sur Hugging Face Hub)
├── data/                # (vide, gitignored — CheXpert-small en local)
└── .env.example
```

## Setup local

### Prérequis
- Python 3.11+
- Compte [Hugging Face](https://huggingface.co/) (hébergement des poids)
- Dataset [CheXpert-small](https://stanfordmlgroup.github.io/competitions/chexpert/) téléchargé dans `data/`

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp ../.env.example ../.env  # puis renseigner HF_TOKEN, HF_MODEL_REPO
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

### Entraînement / fine-tuning

Exploration dans `notebooks/01_exploration.ipynb`, puis version reproductible :

```bash
python train.py --epochs 10 --batch-size 32
```

Entraîné en local sur MacBook Pro (Apple Silicon, accélération **MPS**).

## Roadmap

- [x] Prépa : dataset, repo, environnement
- [ ] Modèle : fine-tuning ResNet50 + métriques (accuracy, AUC)
- [ ] Backend API : upload → preprocessing → inférence → GradCAM
- [ ] Frontend : UI upload + affichage prédiction/confiance/heatmap
- [ ] Polish & déploiement : README, démo vidéo, Render + Streamlit Cloud

## Licence & données

Le dataset CheXpert est distribué sous licence Stanford University School of Medicine Research Use Agreement (usage académique / non-commercial uniquement). Voir [conditions d'usage](https://stanfordmlgroup.github.io/competitions/chexpert/).
