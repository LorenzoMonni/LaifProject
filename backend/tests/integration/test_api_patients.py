def test_create_patient(client):
    response = client.post("/patients/", json={"name": "Mario", "age": 81, "room": "A1"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Mario"
    assert data["age"] == 81

def test_get_patients(client):
    response = client.get("/patients/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
