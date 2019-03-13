import json
import requests
from django.conf import settings
from modulos.servicio.exceptions import ServicioException

TOKEN = getattr(settings, 'SERVICIO_TOKEN', 'mi_token')

class BaseResponse(object):
    def __init__(self, is_valid, message, code, message_type, data):
        self.is_valid = is_valid
        self.message = message
        self.code = code
        self.message_type = message_type
        self.data = data
    @property
    def value(self):
        response = {
            'is_valid': self.is_valid,
            'message': self.message,
            'code': self.code,
            'message_type': self.message_type,
            'data': json.loads(self.data),
        }
        return response

class BaseApi(object):
    base_url = 'https://ws.agetic.gob.bo'

    def request(self, method, path,value, body={}):
        headers = {
            'Authorization': 'Bearer %s' % TOKEN
        }
        path = '%s%s' % (self.base_url, path)
        request_data = requests.request(method, path, headers=headers)
        if 200>= request_data.status_code <= 400:
            values = request_data.json()[value[0]]
            response = BaseResponse(
                is_valid=values['EsValido'],
                message=values['DescripcionRespuesta'],
                code=values['CodigoUnico'],
                message_type=values['CodigoRespuesta'],
                data=values[value[1]],
            ).value
        else:
            raise ServicioException()
        return response