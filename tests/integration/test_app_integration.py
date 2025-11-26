from app.app import app


def test_integration_home():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data.decode() == "Aplicação Flask"


def test_integration_echo():  # <- 2 linhas em branco aqui!
    client = app.test_client()
    payload = {"x": 123}
    resp = client.post("/echo", json=payload)
    assert resp.status_code == 200
    assert resp.json == {"you_sent": payload}