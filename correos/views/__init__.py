from rest_framework.views import APIView as OriginalAPIView
from correos.exceptions import PermissionDenied, UserDoesnotAuthenticated


class APIView(OriginalAPIView):
    def permission_denied(self, request, message=None):
        """Si la solicitud no está permitida, determine qué tipo de excepción elevar."""
        if request.authenticators and not request.successful_authenticator:
            raise UserDoesnotAuthenticated
        raise PermissionDenied(message=message)