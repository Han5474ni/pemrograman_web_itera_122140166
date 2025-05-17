"""
Package initialization for views
"""
from .matakuliah import (
    get_matakuliah_collection,
    get_matakuliah_item,
    create_matakuliah,
    update_matakuliah,
    delete_matakuliah
)
from .notfound import notfound_view
from .auth import login

__all__ = [
    'get_matakuliah_collection',
    'get_matakuliah_item',
    'create_matakuliah',
    'update_matakuliah',
    'delete_matakuliah',
    'notfound_view',
    'login'
]
