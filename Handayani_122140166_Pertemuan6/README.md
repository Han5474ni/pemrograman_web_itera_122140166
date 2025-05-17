# Dokumentasi API Matakuliah dengan Pyramid Framework

## Deskripsi
Dokumentasi ini menjelaskan langkah-langkah pembuatan API sederhana untuk manajemen data matakuliah di perguruan tinggi menggunakan Pyramid Framework, SQLAlchemy, Alembic, dan PostgreSQL.

## Struktur Proyek
```
pyramid_matakuliah_api/
├── matakuliah_api/
│   ├── alembic/                  # Konfigurasi dan migrasi Alembic
│   │   ├── versions/             # File migrasi database
│   │   ├── env.py                # Konfigurasi environment Alembic
│   │   └── script.py.mako        # Template untuk file migrasi
│   ├── matakuliah_api/
│   │   ├── models/               # Model SQLAlchemy
│   │   │   ├── __init__.py
│   │   │   ├── meta.py           # Metadata dan Base class
│   │   │   └── matakuliah.py     # Model Matakuliah
│   │   ├── schemas/              # Schema validasi Marshmallow
│   │   │   ├── __init__.py
│   │   │   └── matakuliah.py     # Schema validasi Matakuliah
│   │   ├── security/             # Modul keamanan dan autentikasi
│   │   │   ├── __init__.py
│   │   │   └── jwt_auth.py       # Implementasi JWT
│   │   ├── views/                # View dan endpoint API
│   │   │   ├── __init__.py
│   │   │   ├── auth.py           # Endpoint autentikasi
│   │   │   ├── matakuliah.py     # Endpoint CRUD matakuliah
│   │   │   └── notfound.py       # Penanganan error 404
│   │   └── __init__.py           # Konfigurasi aplikasi
│   ├── alembic.ini               # Konfigurasi Alembic
│   └── development.ini           # Konfigurasi Pyramid
├── venv/                         # Virtual environment
└── test_api.sh                   # Script pengujian API dengan curl
```

## Langkah-langkah Setup

### 1. Instalasi PostgreSQL
```bash
sudo apt-get update
sudo apt-get install -y postgresql postgresql-contrib
sudo service postgresql start
```

### 2. Setup Virtual Environment dan Instalasi Dependensi
```bash
# Buat direktori proyek
mkdir -p pyramid_matakuliah_api
cd pyramid_matakuliah_api

# Buat dan aktifkan virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Inisialisasi proyek Pyramid
pip install cookiecutter
cookiecutter --no-input https://github.com/Pylons/pyramid-cookiecutter-starter package_name=matakuliah_api project_name="Matakuliah API" template_language=jinja2

# Instalasi dependensi
cd matakuliah_api
pip install -e ".[testing]"
pip install sqlalchemy alembic psycopg2-binary PyJWT marshmallow paginate webargs
```

### 3. Setup Database PostgreSQL
```bash
# Buat user dan database
sudo -u postgres psql -c "CREATE USER matakuliah_user WITH PASSWORD 'matakuliah_password';"
sudo -u postgres psql -c "CREATE DATABASE matakuliah_db OWNER matakuliah_user;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE matakuliah_db TO matakuliah_user;"
```

### 4. Konfigurasi Database di development.ini
Tambahkan konfigurasi berikut di bagian `[app:main]` pada file `development.ini`:
```ini
# Database Configuration
sqlalchemy.url = postgresql://matakuliah_user:matakuliah_password@localhost:5432/matakuliah_db
retry.attempts = 3
```

### 5. Inisialisasi Alembic dan Migrasi Database
```bash
# Inisialisasi Alembic
alembic init alembic

# Konfigurasi alembic.ini
# Ubah sqlalchemy.url = postgresql://matakuliah_user:matakuliah_password@localhost:5432/matakuliah_db

# Buat migrasi
alembic revision --autogenerate -m "create matakuliah table"

# Jalankan migrasi
alembic upgrade head
```

### 6. Menjalankan Server
```bash
# Jalankan server Pyramid
pserve development.ini --reload
```

## Endpoint API

### Autentikasi
- **POST /api/auth/login**
  - Request: `{"username": "admin", "password": "admin123"}`
  - Response: `{"token": "jwt_token", "username": "admin"}`

### Matakuliah
- **GET /api/matakuliah**
  - Headers: `Authorization: Bearer jwt_token`
  - Query Parameters: `page=1&items_per_page=10`
  - Response:
    ```json
    {
      "data": [
        {
          "id": 1,
          "kode_mk": "IF001",
          "nama_mk": "Pemrograman Web",
          "sks": 3,
          "semester": 5
        }
      ],
      "pagination": {
        "page": 1,
        "items_per_page": 10,
        "total_items": 1,
        "total_pages": 1,
        "has_next": false,
        "has_previous": false
      }
    }
    ```

- **GET /api/matakuliah/{id}**
  - Headers: `Authorization: Bearer jwt_token`
  - Response:
    ```json
    {
      "id": 1,
      "kode_mk": "IF001",
      "nama_mk": "Pemrograman Web",
      "sks": 3,
      "semester": 5
    }
    ```

- **POST /api/matakuliah**
  - Headers: `Authorization: Bearer jwt_token`
  - Request:
    ```json
    {
      "kode_mk": "IF001",
      "nama_mk": "Pemrograman Web",
      "sks": 3,
      "semester": 5
    }
    ```
  - Response: Status 201 Created dengan data matakuliah yang dibuat

- **PUT /api/matakuliah/{id}**
  - Headers: `Authorization: Bearer jwt_token`
  - Request:
    ```json
    {
      "nama_mk": "Pemrograman Web Lanjut",
      "sks": 4
    }
    ```
  - Response: Data matakuliah yang diupdate

- **DELETE /api/matakuliah/{id}**
  - Headers: `Authorization: Bearer jwt_token`
  - Response: Status 204 No Content

## Pengujian API dengan curl
Script `test_api.sh` telah disediakan untuk menguji semua endpoint API. Jalankan dengan:
```bash
./test_api.sh
```

## Best Practice dalam Pengembangan API dengan Pyramid

1. **Struktur Modular**
   - Pisahkan kode ke dalam modul-modul terpisah (models, views, schemas, security)
   - Gunakan package initialization (`__init__.py`) untuk mengatur ekspor

2. **Validasi Data**
   - Gunakan Marshmallow untuk validasi data input dan output
   - Definisikan aturan validasi yang jelas (panjang string, rentang nilai)

3. **Autentikasi dan Keamanan**
   - Implementasikan JWT untuk autentikasi API
   - Gunakan HTTPS di lingkungan produksi
   - Jangan hardcode secret key di kode, gunakan environment variable

4. **Penanganan Error**
   - Buat penanganan error yang konsisten
   - Berikan pesan error yang informatif
   - Gunakan HTTP status code yang sesuai

5. **Paginasi**
   - Implementasikan paginasi untuk endpoint yang mengembalikan banyak data
   - Sertakan metadata paginasi dalam respons

6. **Dokumentasi**
   - Dokumentasikan setiap endpoint dengan docstring
   - Jelaskan parameter input dan output
   - Berikan contoh request dan response

7. **Migrasi Database**
   - Gunakan Alembic untuk migrasi database
   - Buat migrasi untuk setiap perubahan skema
   - Jangan mengubah migrasi yang sudah dijalankan

8. **Testing**
   - Buat unit test dan integration test
   - Gunakan fixtures untuk setup data test
   - Otomatisasi testing dengan CI/CD

9. **Versioning API**
   - Pertimbangkan versioning API (misalnya `/api/v1/matakuliah`)
   - Jangan mengubah API yang sudah dipublikasikan tanpa versioning

10. **Logging**
    - Implementasikan logging yang baik
    - Log error dan aktivitas penting
    - Gunakan level log yang sesuai (DEBUG, INFO, ERROR)
