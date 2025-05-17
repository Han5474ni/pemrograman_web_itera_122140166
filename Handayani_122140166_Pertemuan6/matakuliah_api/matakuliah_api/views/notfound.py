from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid.response import Response
import json

@view_config(context=HTTPNotFound)
def notfound_view(request):
    """
    View untuk menangani error 404 Not Found.
    
    Mengembalikan respons JSON dengan status 404 dan pesan error.
    """
    request.response.status = 404
    return Response(
        json_body={"error": "Resource tidak ditemukan"},
        status=404,
        content_type='application/json'
    )
