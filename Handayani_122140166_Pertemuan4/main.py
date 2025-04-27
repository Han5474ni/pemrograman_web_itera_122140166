# Program Utama - main.py

# Import modul-modul yang diperlukan
import math_operations as mo
from math_operations import *
import bmi_calculator as bmi
import data_nilai_mahasiswa as dnm

def tampilkan_menu():
    """Menampilkan menu utama program"""
    print("\n" + "=" * 50)
    print("PERTEMUAN 4".center(50))
    print("=" * 50)
    print("1. Program Penghitung BMI")
    print("2. Program Pengelolaan Data Nilai Mahasiswa")
    print("3. Program Modul Matematika")
    print("0. Keluar")
    print("-" * 50)

def jalankan_program_bmi():
    """Menjalankan program penghitung BMI"""
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
        bmi_nilai, kategori = bmi.hitung_bmi(berat, tinggi)
        
        # Tampilkan hasil
        print("\n----- HASIL PERHITUNGAN -----")
        print(f"BMI Anda: {bmi_nilai:.2f}")
        print(f"Kategori: {kategori}")
        print("-" * 30)
        
    except ValueError:
        print("\nError: Input harus berupa angka!")

def jalankan_program_nilai_mahasiswa():
    """Menjalankan program pengelolaan data nilai mahasiswa"""
    dnm.main()

def jalankan_program_matematika():
    """Menjalankan program modul matematika"""
    print("\n===== PROGRAM MODUL MATEMATIKA =====\n")
    
    # Bagian 1: Menggunakan fungsi dengan import math_operations as mo
    print("MENGGUNAKAN IMPORT DENGAN ALIAS (import math_operations as mo)")
    print("-" * 60)
    
    # Contoh persegi
    sisi_persegi = 5
    print(f"Persegi dengan sisi {sisi_persegi} satuan:")
    print(f"Luas     = {mo.luas_persegi(sisi_persegi):.2f} satuan persegi")
    print(f"Keliling = {mo.keliling_persegi(sisi_persegi):.2f} satuan")
    
    # Contoh persegi panjang
    panjang = 8
    lebar = 4
    print(f"\nPersegi panjang dengan panjang {panjang} dan lebar {lebar} satuan:")
    print(f"Luas     = {mo.luas_persegi_panjang(panjang, lebar):.2f} satuan persegi")
    print(f"Keliling = {mo.keliling_persegi_panjang(panjang, lebar):.2f} satuan")
    
    # Contoh lingkaran
    jari_jari = 7
    print(f"\nLingkaran dengan jari-jari {jari_jari} satuan:")
    print(f"Luas     = {mo.luas_lingkaran(jari_jari):.2f} satuan persegi")
    print(f"Keliling = {mo.keliling_lingkaran(jari_jari):.2f} satuan")
    print(f"Nilai PI yang digunakan: {mo.PI}")
    
    # Bagian 2: Menggunakan fungsi dengan from math_operations import *
    print("\n\nMENGGUNAKAN IMPORT LANGSUNG (from math_operations import *)")
    print("-" * 60)
    
    # Contoh konversi suhu
    suhu_celsius = 25
    print(f"Konversi suhu {suhu_celsius}°C:")
    print(f"Fahrenheit = {celsius_ke_fahrenheit(suhu_celsius):.2f}°F")
    print(f"Kelvin     = {celsius_ke_kelvin(suhu_celsius):.2f}K")
    
    # Contoh perhitungan dengan nilai berbeda
    sisi_persegi2 = 10
    print(f"\nPersegi dengan sisi {sisi_persegi2} satuan:")
    print(f"Luas     = {luas_persegi(sisi_persegi2):.2f} satuan persegi")
    print(f"Keliling = {keliling_persegi(sisi_persegi2):.2f} satuan")
    
    jari_jari2 = 3.5
    print(f"\nLingkaran dengan jari-jari {jari_jari2} satuan:")
    print(f"Luas     = {luas_lingkaran(jari_jari2):.2f} satuan persegi")
    print(f"Keliling = {keliling_lingkaran(jari_jari2):.2f} satuan")
    print(f"Nilai PI yang digunakan: {PI}")

def main():
    """Fungsi utama program"""
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu [0-3]: ")
        
        if pilihan == "1":
            jalankan_program_bmi()
        elif pilihan == "2":
            jalankan_program_nilai_mahasiswa()
        elif pilihan == "3":
            jalankan_program_matematika()
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan program ini!")
            break
        else:
            print("\nError: Pilihan tidak valid! Silakan pilih menu 0-3.")

if __name__ == "__main__":
    main()