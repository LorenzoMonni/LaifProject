def test_add_measurement(client):
    # Otteniamo un paziente esistente
    patients = client.get("/patients/").json()
    pid = patients[0]["id"]

    response = client.post("/measurements/", json={
        "patient_id": pid,
        "heart_rate": 78.5,
        "temperature": 36.8,
        "blood_pressure": 118.0
    })

    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == pid
    assert data["heart_rate"] > 0

def test_summary_endpoint(client):
    patients = client.get("/patients/").json()
    pid = patients[0]["id"]

    res = client.get(f"/patients/{pid}/summary")
    assert res.status_code == 200
    data = res.json()
    assert "avg_heart_rate" in data
