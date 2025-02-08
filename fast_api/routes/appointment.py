from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Appointment, Slot
from schemas import AppointmentCreate, CancelAppointment

router = APIRouter()

@router.get("/{patient_id}")
def get_appointments_by_patient(patient_id: int, db: Session = Depends(get_db)):
    appointments = db.query(Appointment).filter(Appointment.patient_id == patient_id).all()

    if not appointments:
        return {"message": "No appointments found for this patient", "result": False}

    return {"data": appointments, "result": True}

@router.post("/create_appointment")
def create_appointment(appointment_data: AppointmentCreate, db: Session = Depends(get_db)):
    # Fetch slot details to get the date
    slot = db.query(Slot).filter(Slot.id == appointment_data.slot_id).first()

    if not slot:
        return {"message": "Invalid slot ID", "result": False}
    
    # Check if the patient already has an appointment for the same doctor on the same date
    existing_appointment = db.query(Appointment).join(Slot).filter(
        Appointment.patient_id == appointment_data.patient_id,
        Appointment.doctor_id == appointment_data.doctor_id,
        Slot.date == slot.date,
        Appointment.current_status != "Cancelled"
    ).first()

    if existing_appointment:
        return {"message": "You already have an appointment with this doctor on the same date.", "result": False}

    # Create new appointment
    new_appointment = Appointment(
        patient_id=appointment_data.patient_id,
        doctor_id=appointment_data.doctor_id,
        slot_id=appointment_data.slot_id,
        current_status="Booked"
    )
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return {"message": "Appointment created successfully", "appointment_id": new_appointment.id, "result": True}

@router.post("/cancel_appointment")
def cancel_appointment(appointment_data: CancelAppointment, db: Session = Depends(get_db)):
    
    appointment = db.query(Appointment).filter(Appointment.id == appointment_data.id).first()

    if not appointment:
        return {"message": "Appointment not found", "result": False}

    if appointment.current_status == "Cancelled":
        return {"message": "Appointment is already cancelled", "result": False}

    # Updated the status to "Cancelled"
    appointment.current_status = "Cancelled"
    db.commit()
    db.refresh(appointment)

    return {"message": "Appointment cancelled successfully", "result": True}