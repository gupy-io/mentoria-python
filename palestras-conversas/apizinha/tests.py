from starlette.testclient import TestClient


from main import app

client = TestClient(app)


def test_main_status_code():
    resp = client.get("/")
    assert resp.status_code == 200


def test_response():
    resp = client.get("/")
    assert resp.json() == {"classic": "A lua cheia..."}


def test_len_response():
    resp = client.get("/todo")
    assert len(resp.json()) == 3


