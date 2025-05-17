# Todo List Pengembangan API Matakuliah dengan Pyramid

## Persiapan Lingkungan
- [x] Menyiapkan lingkungan virtual Python
- [x] Inisialisasi proyek Pyramid
- [x] Instalasi dependensi (Pyramid, SQLAlchemy, Alembic, psycopg2)
- [x] Instalasi PostgreSQL

## Database Setup
- [x] Membuat database PostgreSQL
- [x] Membuat user dan permission database
- [x] Konfigurasi koneksi database di development.ini

## Model dan Migrasi
- [x] Membuat model data Matakuliah dengan SQLAlchemy
- [x] Inisialisasi Alembic untuk migrasi
- [x] Membuat migrasi untuk tabel matakuliah
- [x] Menjalankan migrasi database

## API Endpoints
- [x] Membuat endpoint GET /api/matakuliah (dengan paginasi)
- [x] Membuat endpoint GET /api/matakuliah/{id}
- [x] Membuat endpoint POST /api/matakuliah
- [x] Membuat endpoint PUT /api/matakuliah/{id}
- [x] Membuat endpoint DELETE /api/matakuliah/{id}
- [x] Menambahkan penanganan error 404

## Autentikasi dan Validasi
- [x] Implementasi autentikasi JWT
- [x] Menambahkan validasi data input

## Testing
- [x] Testing API dengan curl untuk semua endpoint CRUD

## Dokumentasi
- [x] Menambahkan docstring pada kode
- [x] Menyiapkan contoh isi file penting
- [x] Menjelaskan cara menjalankan server dan migrasi
- [x] Memberikan rekomendasi struktur project modular
- [x] Menyusun ringkasan best practice Pyramid API
