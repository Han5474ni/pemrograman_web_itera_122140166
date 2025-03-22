function sapaNama(nama) {
    return `Halo, ${nama}! Selamat belajar Matematika!`;
}

// Event handler untuk tombol sapa
document.getElementById("sapa-button").addEventListener("click", function() {
    const nama = document.getElementById("nama-input").value;
    if (nama.trim() === "") {
        document.getElementById("sapa-output").innerHTML = 
            `<p class="text-red-500">Silakan masukkan nama Anda terlebih dahulu!</p>`;
    } else {
        const pesan = sapaNama(nama);
        document.getElementById("sapa-output").innerHTML = 
            `<p class="text-green-500">${pesan}</p>`;
    }
});


// Fungsi untuk kalkulator
function hitungKalkulator(angka1, angka2, operasi) {
    let hasil;
    switch (operasi) {
        case "tambah":
            hasil = angka1 + angka2;
            break;
        case "kurang":
            hasil = angka1 - angka2;
            break;
        case "kali":
            hasil = angka1 * angka2;
            break;
        case "bagi":
            if (angka2 === 0) return "Error: Pembagian dengan nol tidak diperbolehkan";
            hasil = angka1 / angka2;
            break;
        case "pangkat":
            hasil = Math.pow(angka1, angka2);
            break;
        case "akar":
            if (angka1 < 0) return "Error: Tidak bisa menghitung akar negatif";
            hasil = Math.sqrt(angka1);
            break;
        case "modulus":
            if (angka2 === 0) return "Error: Modulus dengan nol tidak diperbolehkan";
            hasil = angka1 % angka2;
            break;
        default:
            return "Operasi tidak valid";
    }
    return hasil;
}

// Fungsi untuk menangani klik tombol operasi
function kalkulasi(operasi, simbol) {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    const angka2 = parseFloat(document.getElementById("angka2").value);

    if (isNaN(angka1) || (["akar"].includes(operasi) ? false : isNaN(angka2))) {
        document.getElementById("hasil-kalkulator").innerHTML =
            `<p class="text-red-500">Masukkan angka yang valid!</p>`;
    } else {
        const hasil = hitungKalkulator(angka1, angka2, operasi);
        document.getElementById("hasil-kalkulator").innerHTML =
            `<p>Hasil: ${angka1} ${simbol} ${angka2} = ${hasil}</p>`;
    }
}

// Event listener untuk masing-masing tombol
document.getElementById("btn-tambah").addEventListener("click", () => kalkulasi("tambah", "+"));
document.getElementById("btn-kurang").addEventListener("click", () => kalkulasi("kurang", "-"));
document.getElementById("btn-kali").addEventListener("click", () => kalkulasi("kali", "×"));
document.getElementById("btn-bagi").addEventListener("click", () => kalkulasi("bagi", "÷"));
document.getElementById("btn-pangkat").addEventListener("click", () => kalkulasi("pangkat", "^"));
document.getElementById("btn-modulus").addEventListener("click", () => kalkulasi("modulus", "%"));

// Khusus untuk akar (hanya butuh satu angka)
document.getElementById("btn-akar").addEventListener("click", () => {
    const angka1 = parseFloat(document.getElementById("angka1").value);
    if (isNaN(angka1)) {
        document.getElementById("hasil-kalkulator").innerHTML =
            `<p class="text-red-500">Masukkan angka yang valid!</p>`;
    } else {
        const hasil = hitungKalkulator(angka1, 0, "akar");
        document.getElementById("hasil-kalkulator").innerHTML =
            `<p>Hasil: √${angka1} = ${hasil}</p>`;
    }
});
