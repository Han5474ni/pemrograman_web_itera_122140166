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

@view_config(route_name='matakuliah_collection', request_method='POST', renderer='json')
def create_matakuliah(request):
    """
    Endpoint untuk membuat matakuliah baru.
    
    Route: POST /api/matakuliah
    
    Request Body:
        kode_mk (str): Kode matakuliah (wajib)
        nama_mk (str): Nama matakuliah (wajib)
        sks (int): Jumlah SKS (wajib)
        semester (int): Semester (wajib)
    
    Returns:
        dict: Detail matakuliah yang berhasil dibuat
    """
    # Autentikasi
    username = get_user_from_token(request)
    if not username:
        return Response(json_body={"error": "Unauthorized"}, status=401)
    
    # Parse JSON body
    try:
        json_body = request.json_body
    except json.JSONDecodeError:
        return HTTPBadRequest(json_body={"error": "Invalid JSON"})
    
    # Validasi input
    schema = MatakuliahSchema()
    try:
        data = schema.load(json_body)
    except Exception as e:
        return HTTPBadRequest(json_body={"error": str(e)})
    
    # Buat objek matakuliah baru
    matakuliah = Matakuliah(
        kode_mk=data.get('kode_mk'),
        nama_mk=data.get('nama_mk'),
        sks=data.get('sks'),
        semester=data.get('semester')
    )
    
    # Simpan ke database
    try:
        request.dbsession.add(matakuliah)
        request.dbsession.flush()  # Untuk mendapatkan ID
        
        # Serialisasi hasil
        result = schema.dump(matakuliah)
        
        return HTTPCreated(json_body=result)
    except IntegrityError:
        request.dbsession.rollback()
        return HTTPBadRequest(json_body={"error": "Kode matakuliah sudah ada"})

@view_config(route_name='matakuliah_item', request_method='PUT', renderer='json')
def update_matakuliah(request):
    """
    Endpoint untuk mengupdate matakuliah berdasarkan ID.
    
    Route: PUT /api/matakuliah/{id}
    
    Path Parameters:
        id (int): ID matakuliah
    
    Request Body:
        kode_mk (str): Kode matakuliah (opsional)
        nama_mk (str): Nama matakuliah (opsional)
        sks (int): Jumlah SKS (opsional)
        semester (int): Semester (opsional)
    
    Returns:
        dict: Detail matakuliah yang berhasil diupdate
    """
    # Autentikasi
    username = get_user_from_token(request)
    if not username:
        return Response(json_body={"error": "Unauthorized"}, status=401)
    
    # Ambil ID dari URL
    matakuliah_id = request.matchdict['id']
    
    # Parse JSON body
    try:
        json_body = request.json_body
    except json.JSONDecodeError:
        return HTTPBadRequest(json_body={"error": "Invalid JSON"})
    
    try:
        # Query database
        matakuliah = request.dbsession.query(Matakuliah).filter(Matakuliah.id == matakuliah_id).one()
        
        # Validasi input
        schema = MatakuliahSchema(partial=True)
        try:
            data = schema.load(json_body)
        except Exception as e:
            return HTTPBadRequest(json_body={"error": str(e)})
        
        # Update objek matakuliah
        if 'kode_mk' in data:
            matakuliah.kode_mk = data['kode_mk']
        if 'nama_mk' in data:
            matakuliah.nama_mk = data['nama_mk']
        if 'sks' in data:
            matakuliah.sks = data['sks']
        if 'semester' in data:
            matakuliah.semester = data['semester']
        
        # Simpan ke database
        try:
            request.dbsession.flush()
            
            # Serialisasi hasil
            result = schema.dump(matakuliah)
            
            return result
        except IntegrityError:
            request.dbsession.rollback()
            return HTTPBadRequest(json_body={"error": "Kode matakuliah sudah ada"})
    except NoResultFound:
        return HTTPNotFound(json_body={"error": f"Matakuliah dengan ID {matakuliah_id} tidak ditemukan"})

@view_config(route_name='matakuliah_item', request_method='DELETE', renderer='json')
def delete_matakuliah(request):
    """
    Endpoint untuk menghapus matakuliah berdasarkan ID.
    
    Route: DELETE /api/matakuliah/{id}
    
    Path Parameters:
        id (int): ID matakuliah
    
    Returns:
        204 No Content jika berhasil
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
        
        # Hapus dari database
        request.dbsession.delete(matakuliah)
        
        return HTTPNoContent()
    except NoResultFound:
        return HTTPNotFound(json_body={"error": f"Matakuliah dengan ID {matakuliah_id} tidak ditemukan"})
