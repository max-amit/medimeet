from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Patient
from schemas import LoginCreate, PatientCreate

router = APIRouter()

@router.post("/register")
def register(patient_data: PatientCreate, db: Session = Depends(get_db)):
    # Create new patient
    new_patient = Patient(
        fname=patient_data.fname,
        lname=patient_data.lname,
        phone=patient_data.phone,
        password=patient_data.password,
        age=patient_data.age
    )
    
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return {"message": "Patient registered successfully", "result": True}


@router.post("/login")
def signUp(login_data: LoginCreate, db: Session = Depends(get_db)):
    user = db.query(Patient).filter(Patient.phone == login_data.phone).first()
    
    if not user:
        return {"message": "Phone number not registered", "result": False}
    
    if (login_data.password != user.password):
        return {"message": "Invalid credentials", "result": False}

    return {"message": "Login successfully", "patient_id": user.id, "result": True}