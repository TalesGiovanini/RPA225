from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_cpf_valido():
    response = client.post("/executar", json={"command": "Validar CPF 123.456.789-09"})
    assert response.status_code == 200
    assert "CPF válido" in response.json()["resposta"]

def test_comando_gpt():
    response = client.post("/executar", json={"command": "Qual é a capital do Brasil?"})
    assert response.status_code == 200
