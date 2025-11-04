from database import SessionLocal
import models
from datetime import datetime, timedelta
import random

def generate_mock_data():
    db = SessionLocal()
    models.Base.metadata.create_all(bind=db.get_bind())

    if db.query(models.Patient).count() > 0:
        print("♻️ Cancellazione dati precedenti...")
        db.query(models.Measurement).delete()
        db.query(models.Patient).delete()
        db.commit()

    patients = [
        {"name": "Mario Rossi", "age": 82, "room": "A1"},
        {"name": "Lucia Bianchi", "age": 78, "room": "B2"},
        {"name": "Giuseppe Verdi", "age": 90, "room": "C3"},
    ]

    for p in patients:
        patient = models.Patient(**p)
        db.add(patient)
        db.commit()
        db.refresh(patient)

        for i in range(30):
            timestamp = datetime.utcnow() - timedelta(hours=i * 8)
            measurement = models.Measurement(
                patient_id=patient.id,
                heart_rate=random.uniform(60, 100),
                temperature=random.uniform(36, 37.8),
                blood_pressure=random.uniform(110, 145),
                timestamp=timestamp
            )
            db.add(measurement)
        db.commit()

    print("✅ Mock data generati correttamente.")
    db.close()

if __name__ == "__main__":
    generate_mock_data()
