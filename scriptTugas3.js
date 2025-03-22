function validateForm() {
    const nama = document.getElementById("nama").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    
    let errors = [];
    const emailMessage = document.getElementById("email-message");
    const errorContainer = document.getElementById("error-messages");

    emailMessage.innerHTML = "";
    errorContainer.innerHTML = "";

    // Validasi Nama: Minimal 3 karakter
    if (nama.length < 3) {
        errors.push("Nama harus lebih dari 3 karakter.");
    }

    // Validasi Email menggunakan regex
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        errors.push("Email tidak valid.");
    } else {
        emailMessage.innerHTML = `<p class="text-green-500">Email yang digunakan valid</p>`;
    }

    // Validasi Password: Minimal 8 karakter
    if (password.length < 8) {
        errors.push("Password minimal 8 karakter.");
    }

    if (errors.length > 0) {
        errorContainer.innerHTML = `<p class="text-red-500">${errors.join("<br>")}</p>`;
        return false; 
    } else {
        errorContainer.innerHTML = `<p class="text-green-500">Form valid! Siap dikirim.</p>`;
        return true;
    }
}

// Event listener untuk validasi email secara langsung saat mengetik
document.getElementById("email").addEventListener("input", function () {
    const email = this.value.trim();
    const emailMessage = document.getElementById("email-message");
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (emailRegex.test(email)) {
        emailMessage.innerHTML = `<p class="text-green-500">Email yang digunakan valid</p>`;
    } else {
        emailMessage.innerHTML = "";
    }
});
