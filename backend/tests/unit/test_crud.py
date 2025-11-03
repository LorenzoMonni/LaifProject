from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import crud, models, schemas

def setup_module():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def test_create_and_read_patient():
    db: Session = SessionLocal()
    new_patient = schemas.PatientCreate(name="Pino", age=83, room="A2")
    patient = crud.create_patient(db, new_patient)
    assert patient.id is not None

    patients = crud.get_patients(db)
    assert len(patients) == 1
    db.close()
