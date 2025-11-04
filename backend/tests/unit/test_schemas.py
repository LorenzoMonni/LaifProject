


def test_measurement_schema_fields(client):
    patients = client.get("/patients/").json()
    pid = patients[0]["id"]

    response = client.post("/measurements/", json={
        "patient_id": pid,
        "heart_rate": 70,
        "temperature": 36.5,
        "blood_pressure": 120
    })
    data = response.json()
    assert set(data.keys()) == {"id", "patient_id", "heart_rate", "temperature", "blood_pressure", "timestamp"}
