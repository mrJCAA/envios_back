from django.contrib import admin

from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    exclude = ('departamento_id', 'cargo', 'cargo_id', 'password', 'last_login')
    search_fields = ('username', 'nombre_completo', 'numero_documento')
    list_display = ('numero_documento', 'nombre_completo', 'username', 'cargo', 'departamento','is_active')