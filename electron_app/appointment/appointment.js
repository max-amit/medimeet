const API_URL_DOCTORS = "http://127.0.0.1:8000/doctors";
const API_URL_SLOTS = "http://127.0.0.1:8000/slots";
const API_URL_APPOINTMENTS = "http://127.0.0.1:8000/appointments";

// Get doctor_id from URL
const urlParams = new URLSearchParams(window.location.search);
const doctorId = urlParams.get("doctorId");
const patientId = localStorage.getItem("logged_in_patient_id");

if (!doctorId || !patientId) {
    alert("Invalid access. Redirecting to home.");
    window.location.href = "home.html";
}

// Fetch Doctor Details
async function fetchDoctor() {
    try {
        const response = await fetch(`${API_URL_DOCTORS}/${doctorId}`);
        const doctor = await response.json();
        document.getElementById("doctor-name").innerText = doctor.data.fname + " " + doctor.data.lname;
        document.getElementById("doctor-specialty").innerText = doctor.data.specialty;
    } catch (error) {
        document.getElementById("doctor-name").innerText = "Error fetching doctor.";
    }
}

// Fetch Available Slots
async function fetchSlots() {
    try {
        const response = await fetch(`${API_URL_SLOTS}/get_slots_for_doctor`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({"doctor_id": doctorId}),
        });
        const slots = await response.json();
        const slotDropdown = document.getElementById("slot");

        slotDropdown.innerHTML = "";
        if (slots.result) {
            slots.data.forEach(slot => {
                const option = document.createElement("option");
                option.value = slot.id;
                option.textContent = slot.date + " " + slot.start_time + " - " + slot.end_time;
                slotDropdown.appendChild(option);
            });
        }
    } catch (error) {
        document.getElementById("slot").innerHTML = "<option>Error fetching slots</option>";
    }
}

// Book Appointment
async function bookAppointment() {
    const slotId = document.getElementById("slot").value;
    if (!slotId) {
        alert("Please select a slot.");
        return;
    }

    try {
        const response = await fetch(`${API_URL_APPOINTMENTS}/create_appointment`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                patient_id: patientId,
                doctor_id: doctorId,
                slot_id: slotId
            })
        });

        const result = await response.json();
        if (result.result) {
            alert("Appointment booked successfully!");
            window.location.href = "../home/home.html";
        } else {
            alert(result.message);
        }
    } catch (error) {
        alert("Error booking appointment.");
    }
}

// Load doctor details and slots when page loads
window.onload = () => {
    fetchDoctor();
    fetchSlots();
};
