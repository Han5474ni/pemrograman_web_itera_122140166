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
