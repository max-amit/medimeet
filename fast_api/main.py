from fastapi import FastAPI
from routes import patient, doctor, appointment, slot

app = FastAPI()

# Include patient routes
app.include_router(patient.router, prefix="/patients", tags=["Patients"])
app.include_router(doctor.router, prefix="/doctors", tags=["Doctors"])
app.include_router(appointment.router, prefix="/appointments", tags=["Appointments"])
app.include_router(slot.router, prefix="/slots", tags=["Slots"])