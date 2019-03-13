import requests
from django.conf import settings
from django.http import HttpResponse
from modulos.servicio import BaseApi



class SegipApi(BaseApi):

    def get_persona(self, ci, fecha):
        #path = '/segip/v2/personas/%s/' % ci
        path = '/segip/v3/personas/%s?fechaNacimiento=%s' % (ci, fecha)
        response = self.request('get', path, ('ConsultaDatoPersonaEnJsonResult', 'DatosPersonaEnFormatoJson'))
        return response['data']