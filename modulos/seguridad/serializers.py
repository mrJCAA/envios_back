from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'numero_documento',
            'nombre_completo',
            'cargo',
            'cargo_id',
            'departamento',
            'departamento_id',
            'is_active',
            'is_staff'
        )
