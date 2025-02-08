const API_URL = "http://127.0.0.1:8000/patients";

async function sendRequest(endpoint, data) {
    try {
        const response = await fetch(`${API_URL}/${endpoint}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
        });

        return await response.json();
    } catch (error) {
        return { success: false, message: "Network error" };
    }
}

// Toggle between login and register forms
document.getElementById("show-register").addEventListener("click", () => {
    document.getElementById("login-container").style.display = "none";
    document.getElementById("register-container").style.display = "block";
});

document.getElementById("show-login").addEventListener("click", () => {
    document.getElementById("register-container").style.display = "none";
    document.getElementById("login-container").style.display = "block";
});

// Handle Login
document.getElementById("login-btn").addEventListener("click", async () => {
    const phone = document.getElementById("login-phone").value;
    const password = document.getElementById("login-password").value;

    const response = await sendRequest("login", { phone, password });

    document.getElementById("login-message").innerText = response.result 
        ? "Login successful!" 
        : `Login failed: ${response.message}`;

    if (response.result) {
        localStorage.setItem("logged_in_patient_id", response.patient_id);
        window.location.href = "../home/home.html";
    }
});

// Handle Register
document.getElementById("register-btn").addEventListener("click", async () => {
    const fname = document.getElementById("first-name").value;
    const lname = document.getElementById("last-name").value;
    const phone = document.getElementById("register-phone").value;
    const password = document.getElementById("register-password").value;
    const age = parseInt(document.getElementById("register-age").value);

    const response = await sendRequest("register", { fname, lname, phone, password, age });

    document.getElementById("register-message").innerText = response.result 
        ? "Registration successful! Redirecting to login..." 
        : `Registration failed: ${response.message}`;

    if (response.result) {
        setTimeout(() => {
            document.getElementById("register-container").style.display = "none";
            document.getElementById("login-container").style.display = "block";
        }, 2000);
    }
});
