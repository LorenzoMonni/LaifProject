import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import models, schemas, crud
from database import SessionLocal, engine

# Carica .env
load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=os.getenv("API_TITLE", "CareMonitor"))

# CORS per Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "CareMonitor API attiva"}

@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db, patient)

@app.get("/patients/", response_model=list[schemas.Patient])
def get_patients(db: Session = Depends(get_db)):
    return crud.get_patients(db)

@app.post("/measurements/", response_model=schemas.Measurement)
def create_measurement(measurement: schemas.MeasurementCreate, db: Session = Depends(get_db)):
    return crud.create_measurement(db, measurement)

@app.get("/patients/{patient_id}/summary")
def get_summary(patient_id: int, db: Session = Depends(get_db)):
    return crud.get_patient_summary(db, patient_id)
