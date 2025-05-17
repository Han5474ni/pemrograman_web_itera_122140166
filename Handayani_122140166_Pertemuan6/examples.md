# Contoh File Penting

## 1. Model Matakuliah (matakuliah_api/models/matakuliah.py)

```python
from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    UniqueConstraint
)

from .meta import Base


class Matakuliah(Base):
    """
    Model untuk data matakuliah di perguruan tinggi.
    
    Atribut:
        id (int): Primary key untuk tabel matakuliah
        kode_mk (str): Kode unik matakuliah
        nama_mk (str): Nama lengkap matakuliah
        sks (int): Jumlah SKS matakuliah
        semester (int): Semester dimana matakuliah ditawarkan
    """
    __tablename__ = 'matakuliah'
    
    id = Column(Integer, primary_key=True)
    kode_mk = Column(String(20), nullable=False, unique=True)
    nama_mk = Column(String(100), nullable=False)
    sks = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)
    
    def __init__(self, kode_mk, nama_mk, sks, semester):
        """
        Inisialisasi objek Matakuliah baru.
        
        Args:
            kode_mk (str): Kode unik matakuliah
            nama_mk (str): Nama lengkap matakuliah
            sks (int): Jumlah SKS matakuliah
            semester (int): Semester dimana matakuliah ditawarkan
        """
        self.kode_mk = kode_mk
        self.nama_mk = nama_mk
        self.sks = sks
        self.semester = semester
    
    def to_dict(self):
        """
        Mengkonversi objek Matakuliah ke dictionary untuk serialisasi JSON.
        
        Returns:
            dict: Dictionary berisi data matakuliah
        """
        return {
            'id': self.id,
            'kode_mk': self.kode_mk,
            'nama_mk': self.nama_mk,
            'sks': self.sks,
            'semester': self.semester
        }
```

## 2. View Matakuliah (matakuliah_api/views/matakuliah.py)

```python
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest, HTTPCreated, HTTPNoContent
from pyramid.response import Response
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from paginate import Page
import json

from ..models import Matakuliah
from ..schemas import MatakuliahSchema
from ..security import get_user_from_token

@view_config(route_name='matakuliah_collection', request_method='GET', renderer='json')
def get_matakuliah_collection(request):
    """
    Endpoint untuk mendapatkan daftar semua matakuliah dengan paginasi.
    
    Route: GET /api/matakuliah
    
    Query Parameters:
        page (int): Nomor halaman (default: 1)
        items_per_page (int): Jumlah item per halaman (default: 10)
    
    Returns:
        dict: Daftar matakuliah dengan informasi paginasi
    """
    # Autentikasi
    username = get_user_from_token(request)
    if not username:
        return Response(json_body={"error": "Unauthorized"}, status=401)
    
    # Ambil parameter paginasi
    try:
        page = int(request.params.get('page', 1))
        items_per_page = int(request.params.get('items_per_page', 10))
    except ValueError:
        return HTTPBadRequest(json_body={"error": "Parameter paginasi harus berupa angka"})
    
    # Query database
    query = request.dbsession.query(Matakuliah)
    
    # Buat paginasi
    page_obj = Page(
        query,
        page=page,
        items_per_page=items_per_page
    )
    
    # Serialisasi hasil
    schema = MatakuliahSchema(many=True)
    result = schema.dump(page_obj.items)
    
    # Buat response dengan metadata paginasi
    return {
        'data': result,
        'pagination': {
            'page': page,
            'items_per_page': items_per_page,
            'total_items': page_obj.item_count,
            'total_pages': page_obj.page_count,
            'has_next': page_obj.has_next,
            'has_previous': page_obj.has_previous
        }
    }

# Contoh endpoint GET by ID
@view_config(route_name='matakuliah_item', request_method='GET', renderer='json')
def get_matakuliah_item(request):
    """
    Endpoint untuk mendapatkan detail satu matakuliah berdasarkan ID.
    
    Route: GET /api/matakuliah/{id}
    
    Path Parameters:
        id (int): ID matakuliah
    
    Returns:
        dict: Detail matakuliah
    """
    # Autentikasi
    username = get_user_from_token(request)
    if not username:
        return Response(json_body={"error": "Unauthorized"}, status=401)
    
    # Ambil ID dari URL
    matakuliah_id = request.matchdict['id']
    
    try:
        # Query database
        matakuliah = request.dbsession.query(Matakuliah).filter(Matakuliah.id == matakuliah_id).one()
        
        # Serialisasi hasil
        schema = MatakuliahSchema()
        result = schema.dump(matakuliah)
        
        return result
    except NoResultFound:
        return HTTPNotFound(json_body={"error": f"Matakuliah dengan ID {matakuliah_id} tidak ditemukan"})
```

## 3. Schema Validasi (matakuliah_api/schemas/matakuliah.py)

```python
from marshmallow import Schema, fields, validate

class MatakuliahSchema(Schema):
    """
    Schema untuk validasi data matakuliah.
    
    Digunakan untuk validasi input pada endpoint POST dan PUT,
    serta serialisasi output pada semua endpoint.
    """
    id = fields.Integer(dump_only=True)
    kode_mk = fields.String(
        required=True, 
        validate=validate.Length(min=3, max=20),
        error_messages={"required": "Kode matakuliah harus diisi"}
    )
    nama_mk = fields.String(
        required=True, 
        validate=validate.Length(min=3, max=100),
        error_messages={"required": "Nama matakuliah harus diisi"}
    )
    sks = fields.Integer(
        required=True, 
        validate=validate.Range(min=1, max=12),
        error_messages={"required": "SKS harus diisi"}
    )
    semester = fields.Integer(
        required=True, 
        validate=validate.Range(min=1, max=14),
        error_messages={"required": "Semester harus diisi"}
    )
```

## 4. Konfigurasi Alembic (alembic/env.py)

```python
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import models from matakuliah_api
from matakuliah_api.models import Base
from matakuliah_api.models.matakuliah import Matakuliah

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

## 5. Konfigurasi development.ini

```ini
###
# app configuration
# https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/environment.html
###

[app:main]
use = egg:matakuliah_api

pyramid.reload_templates = true
pyramid.debug_authorization = false
pyramid.debug_notfound = false
pyramid.debug_routematch = false
pyramid.default_locale_name = en
pyramid.includes =
    pyramid_debugtoolbar

# Database Configuration
sqlalchemy.url = postgresql://matakuliah_user:matakuliah_password@localhost:5432/matakuliah_db
retry.attempts = 3

# By default, the toolbar only appears for clients from IP addresses
# '127.0.0.1' and '::1'.
# debugtoolbar.hosts = 127.0.0.1 ::1

###
# wsgi server configuration
###

[server:main]
use = egg:waitress#main
listen = localhost:6543

###
# logging configuration
# https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/logging.html
###

[loggers]
keys = root, matakuliah_api

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = INFO
handlers = console

[logger_matakuliah_api]
level = DEBUG
handlers =
qualname = matakuliah_api

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(asctime)s %(levelname)-5.5s [%(name)s:%(lineno)s][%(threadName)s] %(message)s
```

## 6. Contoh Response JSON

### GET /api/matakuliah
```json
{
  "data": [
    {
      "id": 1,
      "kode_mk": "IF001",
      "nama_mk": "Pemrograman Web",
      "sks": 3,
      "semester": 5
    },
    {
      "id": 2,
      "kode_mk": "IF002",
      "nama_mk": "Basis Data",
      "sks": 4,
      "semester": 3
    }
  ],
  "pagination": {
    "page": 1,
    "items_per_page": 10,
    "total_items": 2,
    "total_pages": 1,
    "has_next": false,
    "has_previous": false
  }
}
```

### GET /api/matakuliah/{id}
```json
{
  "id": 1,
  "kode_mk": "IF001",
  "nama_mk": "Pemrograman Web",
  "sks": 3,
  "semester": 5
}
```

### POST /api/matakuliah
```json
{
  "id": 3,
  "kode_mk": "IF003",
  "nama_mk": "Algoritma dan Struktur Data",
  "sks": 4,
  "semester": 2
}
```

### PUT /api/matakuliah/{id}
```json
{
  "id": 1,
  "kode_mk": "IF001",
  "nama_mk": "Pemrograman Web Lanjut",
  "sks": 4,
  "semester": 5
}
```

### DELETE /api/matakuliah/{id}
Status: 204 No Content

### Error 404
```json
{
  "error": "Matakuliah dengan ID 999 tidak ditemukan"
}
```

### Error Validasi
```json
{
  "error": "{'kode_mk': ['Shorter than minimum length 3.'], 'sks': ['Must be greater than or equal to 1.']}"
}
```
