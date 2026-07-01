"""
Tests de l'API FastAPI.
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# TODO: test_predict_endpoint (upload image de test + vérif structure réponse)
