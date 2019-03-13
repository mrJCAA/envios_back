from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import APIException

class ServicioException(APIException):
    status_code = 500
    default_detail = {
        'message': _('Problemas en la conexion'),
        'type': 'error',
        'status': status_code
    }
    default_code = 'not_authenticated'