# Program Penghitung BMI (Body Mass Index)

def hitung_bmi(berat, tinggi):
    """
    Fungsi untuk menghitung BMI dan menentukan kategori berat badan
    
    Args:
        berat (float): Berat badan dalam kilogram (kg)
        tinggi (float): Tinggi badan dalam meter (m)
        
    Returns:
        tuple: (nilai_bmi, kategori)
    """
    # Hitung BMI menggunakan rumus: BMI = berat / (tinggi * tinggi)
    bmi = berat / (tinggi * tinggi)
    
    # Tentukan kategori berdasarkan nilai BMI
    if bmi < 18.5:
        kategori = "Berat badan kurang"
    elif 18.5 <= bmi < 25:
        kategori = "Berat badan normal"
    elif 25 <= bmi < 30:
        kategori = "Berat badan berlebih"
    else:  # BMI >= 30
        kategori = "Obesitas"
    
    return bmi, kategori

# Program utama
def main():
    print("\n===== PROGRAM PENGHITUNG BMI =====\n")
    
    # Input dari pengguna
    try:
        berat = float(input("Masukkan berat badan (kg): "))
        tinggi = float(input("Masukkan tinggi badan (m): "))
        
        # Validasi input
        if berat <= 0 or tinggi <= 0:
            print("\nError: Berat dan tinggi harus bernilai positif!")
            return
        
        # Hitung BMI dan dapatkan kategori
        bmi, kategori = hitung_bmi(berat, tinggi)
        
        # Tampilkan hasil
        print("\n----- HASIL PERHITUNGAN -----")
        print(f"BMI Anda: {bmi:.2f}")
        print(f"Kategori: {kategori}")
        print("-" * 30)
        
    except ValueError:
        print("\nError: Input harus berupa angka!")

# Jalankan program jika file ini dieksekusi langsung
if __name__ == "__main__":
    main()