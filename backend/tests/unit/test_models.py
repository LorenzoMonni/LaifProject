from models import Patient, Measurement
from datetime import datetime

def test_create_patient_model():
    p = Patient(name="Test", age=80, room="Z1")
    assert p.name == "Test"
    assert p.age == 80
    assert p.room == "Z1"

def test_create_measurement_model():
    m = Measurement(
        patient_id=1,
        heart_rate=75.0,
        temperature=36.7,
        blood_pressure=120.0,
        timestamp=datetime.utcnow()
    )
    assert m.heart_rate > 0
    assert 35 < m.temperature < 40
