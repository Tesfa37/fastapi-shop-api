from fastapi.testclient import TestClient
from fastapi_shop_api.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}
