from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Doctor
from schemas import DoctorCreate

router = APIRouter()

@router.get("/get_all_doctors")
def get_all_doctors(db: Session = Depends(get_db)):
    
    doctors = db.query(Doctor).all()

    if not doctors:
        return {"message": "No doctors found", "result": False}
    
    return {"data": doctors, "message": "Doctors found", "result": True}

@router.get("/{doctor_id}")
def get_doctor_detail(doctor_id: int, db: Session = Depends(get_db)):
    
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()

    if not doctor:
        return {"message": "No doctor found", "result": False}
    
    return {"data": doctor, "message": "doctor found", "result": True}

@router.post("/add_doctors")
def add_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    # Create a new doctor record
    new_doctor = Doctor(
        fname=doctor.fname,
        lname=doctor.lname,
        specialty=doctor.specialty,
        experience=doctor.experience
    )

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    return {"message": "Doctor added successfully", "doctor_id": new_doctor.id, "result": True}