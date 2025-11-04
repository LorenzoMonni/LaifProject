"""
 Create Retrieve Update Delete File
"""


from sqlalchemy.orm import Session
import models, schemas
from statistics import mean

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patients(db: Session):
    return db.query(models.Patient).all()

def create_measurement(db: Session, measurement: schemas.MeasurementCreate):
    db_measurement = models.Measurement(**measurement.dict())
    db.add(db_measurement)
    db.commit()
    db.refresh(db_measurement)
    return db_measurement

def get_patient_summary(db: Session, patient_id: int):
    m = db.query(models.Measurement).filter(models.Measurement.patient_id == patient_id).all()
    if not m:
        return {"message": "No data yet"}
    return {
        "avg_heart_rate": mean([x.heart_rate for x in m]),
        "avg_temp": mean([x.temperature for x in m]),
        'avg_temperature': mean([x.temperature for x in m]),
        'avg_blood_pressure': mean([x.blood_pressure for x in m]),
        "total_measurements": len(m),
    }
