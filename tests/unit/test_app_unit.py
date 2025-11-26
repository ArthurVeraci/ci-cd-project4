from app import app

def test_home_status_code():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert "Aplicação Flask" in r.get_data(as_text=True)

def test_echo():
    client = app.test_client()
    payload = {"msg": "hello"}
    r = client.post("/echo", json=payload)
    assert r.status_code == 200
    data = r.get_json()
    assert data["you_sent"] == payload
