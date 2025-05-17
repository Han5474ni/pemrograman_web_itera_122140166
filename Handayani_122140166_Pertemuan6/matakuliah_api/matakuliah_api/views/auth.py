from pyramid.view import view_config
from pyramid.response import Response
from ..security import generate_jwt_token

@view_config(route_name='auth_login', request_method='POST', renderer='json')
def login(request):
    """
    Endpoint untuk login dan mendapatkan token JWT.
    
    Route: POST /api/auth/login
    
    Request Body:
        username (str): Username untuk login
        password (str): Password untuk login
    
    Returns:
        dict: Token JWT jika berhasil login
    """
    try:
        json_body = request.json_body
        username = json_body.get('username')
        password = json_body.get('password')
        
        # Untuk demo, kita hanya memeriksa username dan password sederhana
        # Pada implementasi nyata, gunakan autentikasi yang lebih aman
        if username == 'admin' and password == 'admin123':
            token = generate_jwt_token(username)
            return {
                'token': token,
                'username': username
            }
        else:
            return Response(
                json_body={"error": "Username atau password salah"},
                status=401
            )
    except Exception as e:
        return Response(
            json_body={"error": str(e)},
            status=400
        )
