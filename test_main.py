from fastapi.testclient import TestClient

from .main import app


client = TestClient(app)


def test_check_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_get_employees():
    response = client.get("/employees/{employee_id}")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "Bob"}, {"id":2, "name": "Pedro"}]