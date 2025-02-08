from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Time
from sqlalchemy.orm import relationship
from database import engine, Base
from datetime import time

# Define the Patient model
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String(100), nullable=False)
    lname = Column(String(100), nullable=False)
    phone = Column(String(15), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)

# Define the Doctor model
class Doctor(Base):
    __tablename__ = "doctors"
    
    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String(100), nullable=False)
    lname = Column(String(100), nullable=False)
    specialty = Column(String(100), nullable=False)
    experience = Column(Integer, nullable=False)

# Define the Slot model
class Slot(Base):
    __tablename__ = "slots"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    date = Column(String(50), nullable=False)
    start_time = Column(String(50), nullable=False)
    end_time = Column(String(50), nullable=False)

    doctor = relationship("Doctor")

# Define the Appointment model
class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    slot_id = Column(Integer, ForeignKey("slots.id"), nullable=False)
    current_status = Column(String(50), nullable=False)

    doctor = relationship("Doctor")
    patient = relationship("Patient")
    slot = relationship("Slot")

# Create all tables in the database
Base.metadata.create_all(bind=engine)