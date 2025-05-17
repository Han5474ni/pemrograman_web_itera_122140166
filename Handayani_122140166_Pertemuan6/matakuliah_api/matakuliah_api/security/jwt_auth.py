import datetime
import jwt
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, Everyone, Authenticated

# Konfigurasi JWT
JWT_SECRET = 'matakuliah-api-jwt-secret'
JWT_ALGORITHM = 'HS256'
JWT_EXPIRATION = 3600  # 1 jam dalam detik

class Root:
    """
    Root factory untuk security ACL.
    
    Mendefinisikan permission untuk akses API.
    """
    __acl__ = [
        (Allow, Authenticated, 'view'),
        (Allow, Authenticated, 'create'),
        (Allow, Authenticated, 'edit'),
        (Allow, Authenticated, 'delete'),
    ]
    
    def __init__(self, request):
        self.request = request

def generate_jwt_token(username):
    """
    Membuat JWT token untuk autentikasi.
    
    Args:
        username (str): Username untuk disimpan dalam token
        
    Returns:
        str: JWT token yang dihasilkan
    """
    payload = {
        'sub': username,
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXPIRATION)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def validate_jwt_token(token):
    """
    Memvalidasi JWT token.
    
    Args:
        token (str): JWT token untuk divalidasi
        
    Returns:
        dict: Payload dari token jika valid, None jika tidak valid
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def get_user_from_token(request):
    """
    Mendapatkan user dari token di header Authorization.
    
    Args:
        request: Request Pyramid
        
    Returns:
        str: Username jika token valid, None jika tidak valid
    """
    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Bearer '):
        return None
    
    token = auth_header.split(' ')[1]
    payload = validate_jwt_token(token)
    
    if payload:
        return payload.get('sub')
    return None

def includeme(config):
    """
    Konfigurasi security untuk aplikasi.
    
    Args:
        config: Pyramid configurator
    """
    # Setup authentication
    authn_policy = AuthTktAuthenticationPolicy('matakuliah-api-secret', callback=None, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.set_root_factory(Root)
