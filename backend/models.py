from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    room = Column(String)
    measurements = relationship("Measurement", back_populates="patient", cascade="all, delete-orphan")

class Measurement(Base):
    __tablename__ = "measurements"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    heart_rate = Column(Float)
    temperature = Column(Float)
    blood_pressure = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    patient = relationship("Patient", back_populates="measurements")
