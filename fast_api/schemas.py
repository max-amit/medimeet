from pydantic import BaseModel
from typing import Optional

class PatientCreate(BaseModel):
    fname: str
    lname: str
    phone: str
    password: str
    age: Optional[int] = None

class LoginCreate(BaseModel):
    phone: str
    password: str

class DoctorCreate(BaseModel):
    fname: str
    lname: str
    experience: int
    specialty: str

class SlotCreate(BaseModel):
    doctor_id: int
    date: str
    start_time: str
    end_time: str

class SlotForDoctor(BaseModel):
    doctor_id: int

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    slot_id: int

class CancelAppointment(BaseModel):
    id: int