from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Slot
from schemas import SlotCreate, SlotForDoctor

router = APIRouter()

@router.post("/add_slots")
def add_slots(slot_data: SlotCreate, db: Session = Depends(get_db)):
    # Create a new Slot record
    new_slot = Slot(
        doctor_id=slot_data.doctor_id,
        date=slot_data.date,
        start_time=slot_data.start_time,
        end_time=slot_data.end_time
    )

    db.add(new_slot)
    db.commit()
    db.refresh(new_slot)

    return {"message": "Slot added successfully", "slot_id": new_slot.id, "result": True}

@router.get("/{slot_id}")
def get_slot_detail(slot_id: int, db: Session = Depends(get_db)):
    slot = db.query(Slot).filter(Slot.id == slot_id).first()

    if not slot:
        return {"message": "No slot found", "result": False}
    
    return {"data": slot, "message": "Slot found", "result": True}

@router.post("/get_slots_for_doctor")
def get_slot_for_doctor(slotData: SlotForDoctor, db: Session = Depends(get_db)):
    slot = db.query(Slot).filter(Slot.doctor_id == slotData.doctor_id).all()
    
    if not slot:
        return {"message": "No slot found", "result": False}

    return {"message": "Slot found", "data": slot, "result": True}