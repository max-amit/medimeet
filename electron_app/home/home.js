const API_URL_DOCTORS = "http://127.0.0.1:8000/doctors";
const API_URL_APPOINTMENTS = "http://127.0.0.1:8000/appointments";
const API_URL_SLOTS = "http://127.0.0.1:8000/slots";

// Fetch and display doctors
async function loadDoctors() {
    try {
        const response = await fetch(`${API_URL_DOCTORS}/get_all_doctors`);
        const doctors = await response.json();
        const doctorList = document.getElementById("doctor-list");

        if (doctors.result) {
            if (doctors.data.length === 0) {
                doctorList.innerHTML = "<p>No doctors available.</p>";
                return;
            }
            doctorList.innerHTML = "";
            doctors.data.forEach(doctor => {
                const div = document.createElement("div");
                div.classList.add("doctor");
                div.innerHTML = `<strong>${doctor.fname} ${doctor.lname}</strong> - ${doctor.specialty} - ${doctor.experience} Exp.`;
                div.onclick = () => bookAppointment(doctor.id);
                doctorList.appendChild(div);
            });
        } else {
            document.getElementById("doctor-list").innerHTML = doctors.message;
        }
    } catch (error) {
        document.getElementById("doctor-list").innerHTML = "<p>Failed to load doctors.</p>";
    }
}

// Fetch and display upcoming appointments
async function loadAppointments() {
    try {
        const patientId = localStorage.getItem("logged_in_patient_id");
        const response = await fetch(`${API_URL_APPOINTMENTS}/${patientId}`);
        const appointments = await response.json();
        const appointmentList = document.getElementById("appointment-list");

        if (appointments.result) {
            if (appointments.data.length === 0) {
                appointmentList.innerHTML = "<p>No upcoming appointments.</p>";
                return;
            }

            appointmentList.innerHTML = "";

            for (const appointment of appointments.data) {
                const doctor = await fetchDoctor(appointment.doctor_id);
                const slot = await fetchSlot(appointment.slot_id);

                const div = document.createElement("div");
                div.classList.add("appointment");

                const cancelButton = appointment.current_status === "Booked"
                    ? `<button onclick="cancelAppointment('${appointment.id}')">Cancel</button>`
                    : "";

                div.innerHTML = `
                <strong>Dr. ${doctor.data.fname} ${doctor.data.lname}</strong> - ${doctor.data.specialty} - ${doctor.data.experience} Exp.<br>
                <strong>Slot:</strong> ${slot.data.date}  ${slot.data.start_time}-${slot.data.end_time}<br>
                <strong>Current Status:</strong> ${appointment.current_status}<br>
                ${cancelButton}
            `;
                appointmentList.appendChild(div);
            }
        } else {
            document.getElementById("appointment-list").innerHTML = appointments.message;
        }
    } catch (error) {
        document.getElementById("appointment-list").innerHTML = "<p>Failed to load appointments.</p>";
    }
}

async function fetchDoctor(doctorId) {
    try {
        const response = await fetch(`${API_URL_DOCTORS}/${doctorId}`);
        return await response.json();
    } catch (error) {
        return { name: "Unknown", specialty: "N/A" };
    }
}

async function fetchSlot(slotId) {
    try {
        const response = await fetch(`${API_URL_SLOTS}/${slotId}`);
        return await response.json();
    } catch (error) {
        return { time: "Unknown Time" };
    }
}

// Cancel appointment
async function cancelAppointment(appointmentId) {
    try {
        await fetch(`${API_URL_APPOINTMENTS}/cancel_appointment/`, {method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({"id": appointmentId})});
        alert("Appointment cancelled!");
        loadAppointments(); // Refresh list
    } catch (error) {
        alert("Failed to cancel appointment.");
    }
}

// Redirect to appointment page
function bookAppointment(doctorId) {
    window.location.href = `../appointment/appointment.html?doctorId=${doctorId}`;
}

// Load data when the page loads
window.onload = () => {
    loadDoctors();
    loadAppointments();
};
