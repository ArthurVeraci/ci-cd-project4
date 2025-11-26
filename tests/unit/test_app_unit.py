from app.app import app


def test_home():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data.decode() == "Aplicação Flask"


def test_echo():  # <- 2 linhas em branco aqui!
    client = app.test_client()
    resp = client.post("/echo", json={"msg": "hello"})
    assert resp.status_code == 200
    assert resp.json == {"you_sent": {"msg": "hello"}}
    