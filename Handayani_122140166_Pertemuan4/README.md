# Program Integrasi Modul Python

Program ini merupakan aplikasi konsol Python yang mengintegrasikan tiga modul berbeda dalam satu antarmuka menu. Program dibuat sebagai bagian dari tugas Praktikum Pemrograman Web ITERA.

## Deskripsi

Program ini terdiri dari tiga modul utama yang diintegrasikan dalam satu aplikasi:

1. **Program Penghitung BMI** - Menghitung Body Mass Index (BMI) berdasarkan berat dan tinggi badan, kemudian menentukan kategori berat badan.
2. **Program Pengelolaan Data Nilai Mahasiswa** - Menampilkan dan menganalisis data nilai mahasiswa, termasuk perhitungan nilai akhir dan penentuan grade.
3. **Program Modul Matematika** - Demonstrasi penggunaan modul matematika untuk perhitungan geometri dan konversi suhu dengan dua metode import yang berbeda.

## Struktur File

Program terdiri dari beberapa file Python:

- `main.py` - Program utama yang mengintegrasikan semua modul dan menampilkan menu
- `bmi_calculator.py` - Modul untuk menghitung BMI dan menentukan kategori berat badan
- `data_nilai_mahasiswa.py` - Modul untuk mengelola dan menampilkan data nilai mahasiswa
- `math_operations.py` - Modul yang berisi fungsi-fungsi matematika dan konversi suhu

## Cara Penggunaan

1. Pastikan Python sudah terinstal di komputer Anda
2. Jalankan file `main.py` dengan perintah:
   ```
   python main.py
   ```
3. Pilih menu yang tersedia dengan memasukkan angka 1-3:
   - **1** - Program Penghitung BMI
   - **2** - Program Pengelolaan Data Nilai Mahasiswa
   - **3** - Program Modul Matematika
   - **0** - Keluar dari program

## Detail Modul

### 1. Program Penghitung BMI

Modul ini menghitung BMI berdasarkan rumus: BMI = berat / (tinggi * tinggi)

Kategori BMI:
- < 18.5: Berat badan kurang
- 18.5 - 24.9: Berat badan normal
- 25 - 29.9: Berat badan berlebih
- ≥ 30: Obesitas

### 2. Program Pengelolaan Data Nilai Mahasiswa

Modul ini menampilkan data nilai mahasiswa dalam bentuk tabel, menghitung nilai akhir dengan bobot:
- 30% UTS
- 40% UAS
- 30% Tugas

Grade ditentukan berdasarkan nilai akhir:
- A: ≥ 80
- B: 70 - 79.9
- C: 60 - 69.9
- D: 50 - 59.9
- E: < 50

Modul juga menampilkan mahasiswa dengan nilai tertinggi dan terendah.

### 3. Program Modul Matematika

Modul ini mendemonstrasikan dua cara import modul:
- `import math_operations as mo` - Import dengan alias
- `from math_operations import *` - Import langsung

Fungsi-fungsi yang tersedia:
- Perhitungan luas dan keliling: persegi, persegi panjang, dan lingkaran
- Konversi suhu: Celsius ke Fahrenheit dan Kelvin

## Contoh Output

### Menu Utama
```
==================================================
                    PERTEMUAN 4                    
==================================================
1. Program Penghitung BMI
2. Program Pengelolaan Data Nilai Mahasiswa
3. Program Modul Matematika
0. Keluar
--------------------------------------------------
```

## Informasi Tambahan

Program ini dikembangkan sebagai bagian dari tugas Praktikum Pemrograman Web pertemuan 4 

NIM: 122140166
