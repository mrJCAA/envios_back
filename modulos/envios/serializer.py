from rest_framework import serializers

from .models import (
    Pais,
    Departamento,
    Cargo,
    Oficina,
    Envio,
    Ciudad
)


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = (
            'id',
            'nombre',
            'sigla',
            'codigo_postal',
            'codigo_pais',
            'icono',
            'fecha_creacion',
        )


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = (
            """completar campos"""
        )


class OficinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oficina
        fields = (
            """Completar campos"""
        )

class EnvioSerializer(serializers.ModelSerializer):
    pais = PaisSerializer(many=True, read_only=True)
    pais_rem_id=serializers.IntegerField(write_only=True)
    pais_des_id=serializers.IntegerField(write_only=True)
    departamento = DepartamentoSerializer(many=True, read_only=True)
    departamento_rem_id=serializers.IntegerField(write_only=True)
    departamento_des_id=serializers.IntegerField(write_only=True)
    ciudad = CiudadSerializer(many=True, read_only=True)
    ciudad_rem_id = serializers.IntegerField(write_only=True)
    ciudad_des_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Envio
        fields = '__all__'
        extra_fields = [
            'pais_rem_id_id',
            'pais_des_id_id',
            'departamento_rem_id_id',
            'departamento_des_id_id',
            'ciudad_rem_id',
            'ciudad_des_id'
        ]