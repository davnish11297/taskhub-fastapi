import requests

BASE_URL = "http://localhost:8000"

def test_health():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_root():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200
    assert "TaskHub" in r.json()["message"]