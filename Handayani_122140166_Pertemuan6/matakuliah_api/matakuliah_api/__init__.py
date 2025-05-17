from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import configure_mappers
import zope.sqlalchemy

# Import models to register them with SQLAlchemy
from .models import (
    Matakuliah,
)

def get_engine(settings, prefix='sqlalchemy.'):
    """
    Membuat SQLAlchemy engine dari konfigurasi.
    
    Args:
        settings: Pyramid settings
        prefix: Prefix untuk konfigurasi SQLAlchemy
        
    Returns:
        SQLAlchemy engine
    """
    return engine_from_config(settings, prefix)

def get_session_factory(engine):
    """
    Membuat session factory dari engine.
    
    Args:
        engine: SQLAlchemy engine
        
    Returns:
        SQLAlchemy session factory
    """
    factory = sessionmaker()
    factory.configure(bind=engine)
    return factory

def get_tm_session(session_factory, transaction_manager):
    """
    Membuat session yang terintegrasi dengan transaction manager.
    
    Args:
        session_factory: SQLAlchemy session factory
        transaction_manager: Transaction manager
        
    Returns:
        SQLAlchemy session
    """
    dbsession = session_factory()
    zope.sqlalchemy.register(
        dbsession, transaction_manager=transaction_manager)
    return dbsession

def main(global_config, **settings):
    """
    Fungsi main untuk aplikasi Pyramid.
    
    Args:
        global_config: Konfigurasi global
        settings: Konfigurasi aplikasi
        
    Returns:
        Pyramid WSGI application
    """
    config = Configurator(settings=settings)
    
    # Konfigurasi SQLAlchemy
    config.include('pyramid_tm')
    
    # Pastikan model SQLAlchemy terdaftar
    configure_mappers()
    
    # Konfigurasi session
    engine = get_engine(settings)
    session_factory = get_session_factory(engine)
    config.registry['dbsession_factory'] = session_factory
    
    # Tambahkan dbsession ke request
    def add_dbsession_to_request(request):
        # Tambahkan dbsession ke request
        transaction_manager = request.tm
        dbsession = get_tm_session(
            session_factory, transaction_manager)
        return dbsession
    
    config.add_request_method(
        add_dbsession_to_request, 'dbsession', reify=True)
    
    # Konfigurasi security
    config.include('.security.jwt_auth')
    
    # Konfigurasi routes
    config.add_route('matakuliah_collection', '/api/matakuliah')
    config.add_route('matakuliah_item', '/api/matakuliah/{id}')
    config.add_route('auth_login', '/api/auth/login')
    
    # Scan views
    config.scan('.views')
    
    return config.make_wsgi_app()
