"""
Frontend Streamlit : upload d'une radiographie, appel à l'API,
affichage de la prédiction, confiance, et heatmap GradCAM.
"""

import streamlit as st

st.set_page_config(page_title="Medical Imaging Classification", layout="centered")

st.title("Classification de radiographies thoraciques")
st.caption("Démo — projet portfolio, usage non-clinique / non-diagnostique.")

# TODO:
#   - st.file_uploader pour l'image
#   - appel POST vers API_BASE_URL/predict
#   - affichage: image originale | heatmap GradCAM côte à côte
#   - affichage: label prédit + barre de confiance
