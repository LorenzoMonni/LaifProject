from pydantic import BaseModel
from datetime import datetime

class MeasurementBase(BaseModel):
    heart_rate: float
    temperature: float
    blood_pressure: float

class MeasurementCreate(MeasurementBase):
    patient_id: int

class Measurement(MeasurementBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class PatientBase(BaseModel):
    name: str
    age: int
    room: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    measurements: list[Measurement] = []

    class Config:
        orm_mode = True
