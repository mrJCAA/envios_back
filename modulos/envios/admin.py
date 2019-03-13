from datetime import datetime as dt
from django.contrib import admin

from correos.admin import ModelLogAdmin

from .models import (
    Pais,
    Departamento,
    Cargo,
    Oficina,
    Envio)

@admin.register(Pais)
class PaisAdmin(ModelLogAdmin):
    list_display = ('nombre',
                    'sigla',
                    'codigo_postal',
                    'codigo_pais',
                    'icono',
                    'usuario_creacion',
                    'fecha_creacion',
                    'usuario_modificacion',
                    'fecha_modificacion')


@admin.register(Departamento)
class DepartamentoAdmin(ModelLogAdmin):
    pass


@admin.register(Cargo)
class CargoAdmin(ModelLogAdmin):
    pass


@admin.register(Oficina)
class OficinaAdmin(ModelLogAdmin):
    pass