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
