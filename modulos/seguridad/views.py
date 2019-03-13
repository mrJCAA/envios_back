from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AnonymousUser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from correos.response import ErrorRestResponse
from correos.exceptions import UserDoesnotAuthenticated
from .serializers import UsuarioSerializer

@api_view(['GET'])
def usuario_actual(request):
    usuario = request.user
    print(request.user)
    if usuario == AnonymousUser():
        raise UserDoesnotAuthenticated()
    serializer = UsuarioSerializer(usuario)
    return Response(serializer.data)