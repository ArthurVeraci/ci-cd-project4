import requests
import time

BASE = "http://localhost:5000"

def test_home_up():
    r = requests.get(f"{BASE}/", timeout=5)
    assert r.status_code == 200

def test_slow_endpoint():
    t0 = time.time()
    r = requests.get(f"{BASE}/slow", timeout=5)
    t = time.time() - t0
    assert r.status_code == 200
    assert t >= 0.2
