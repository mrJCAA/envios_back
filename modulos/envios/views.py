from datetime import datetime as dt
from django.utils.translation import ugettext as _
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from correos.response import ErrorRestResponse, SuccessRestResponse
from correos.viewsets import ViewSet
from correos.views import APIView
from modulos.servicio.servicio import SegipApi
from .serializer import (
    PaisSerializer,
    DepartamentoSerializer,
    CargoSerializer,
    OficinaSerializer,
    EnvioSerializer
)
from .models import (
    Pais,
    Departamento,
    Cargo,
    Oficina,
    Envio
)

class PersonaSegipView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kargs):
        segip_api = SegipApi()
        fecha_nacimiento = dt.strptime(kargs.get('fecha'),'%d-%m-%Y')
        nueva_fecha = dt.strftime(fecha_nacimiento, '%d/%m/%Y')
        datos_persona = segip_api.get_persona(kargs.get('pk'), nueva_fecha)
        
        if datos_persona['Complemento']:
            datos_persona['NumeroDocumento'] += ('-' + datos_persona['Complemento'])
            datos_persona['LugarNacimiento'] = '%s - %s - %s - %s' % (
                datos_persona['LugarNacimientoPais'],
                datos_persona['LugarNacimientoDepartamento'],
                datos_persona['LugarNacimientoProvincia'],
                datos_persona['LugarNacimientoLocalidad'],
            )
            
        return Response(datos_persona)


class PaisView(APIView):
    """Listar todos los paises"""
    def get(self, request, *args, **kargs):
        paises = Pais.objects.filter(fecha_eliminacion__isnull=True)
        serializer = PaisSerializer(paises, many=True)
        return Response(serializer.data)
    
    """Registra un nuevo pais"""
    def post(self, request):
        serializer = PaisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario_creacion=request.user.id, fecha_creacion=dt.now())
            return SuccessRestResponse(_('Registro agregado de manera correcta'), status=status.HTTP_201_CREATED, data=serializer.data)
        return ErrorRestResponse(_('Tiene los siguientes errores'),status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class DepartamentoView(APIView):
    """Lista todos los envios registrados"""
    def get(self, request, *args, **kargs):    
        departamento = Departamento.objects.filter(fecha_eliminacion__isnull=True)
        serializer = DepartamentoSerializer(departamento, many=True)
        return Response(serializer.data)


class CargoView(APIView):
    pass


class EnvioView(APIView):
    permission_classes = (IsAuthenticated,)

    """Lista todos los envios registrados"""
    def get(self, request, *args, **kargs):    
        envio = Envio.objects.filter(fecha_eliminacion__isnull=True)
        serializer = EnvioSerializer(envio, many=True)
        return Response(serializer.data)

    """Crea un nuevo registro de envio"""
    def post(self, request):
        serializer = EnvioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                usuario_creacion=request.user.id,
                pais_rem_id=serializer.validated_data.get('pais_rem_id'),
                pais_des_id=serializer.validated_data.get('pais_des_id'),
                departamento_rem_id=serializer.validated_data.get('departamento_rem_id'),
                departamento_des_id=serializer.validated_data.get('departamento_des_id')
            )
            return SuccessRestResponse(_('Registro agregado de manera correcta'), status=status.HTTP_201_CREATED, data=serializer.data)
        return ErrorRestResponse(_('Tiene los siguientes errores'), status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class EnvioViewDetail(APIView):
    """Retorna el detalle de un Envio"""
    def get(self, request, *args, **kargs):
        try:
            envio = Envio.objects.get(id=kargs.get('pk'))
            return Response(EnvioSerializer(envio).data)
        except Envio.DoesNotExist:
            return ErrorRestResponse(_('Recurso no encontrado'), status=status.HTTP_404_NOT_FOUND)
    
    """Este metodo actualiza a un envio"""
    def put(self, request, *args, **kargs):
        envio = Envio.objects.get(id=kargs.get('pk'))
        serializer = EnvioSerializer(envio, data=request.data)
        try:
            if serializer.is_valid():
                serializer.save(usuario_modificacion=request.user.id, fecha_modificacion=dt.now())
                return SuccessRestResponse(_('Registro actualizado de manera correcta'), status=status.HTTP_201_CREATED, data=serializer.data)
        except Aeropuerto.DoesNotExist:
            return ErrorRestResponse(_('Tiene los siguientes errores'), status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
