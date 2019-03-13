from django.db import models

from django.utils.translation import ugettext as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UsuarioManager(BaseUserManager):
    """Manager de modelos de Usuario del modulo de seguridad"""
    def _create_user(self, username, email, numero_documento, nombre_completo, password, is_staff, is_superuser, **kwargs):
        """Funcion que realiza el registro de un usuario dentro del sistema"""
        now = timezone.now()
        if not email:
            raise ValueError(_('Debe Proporcionar un correo electronico'))
        email = self.normalize_email(email)
        user = self.model(
            username = username,
            numero_documento = numero_documento,
            nombre_completo = nombre_completo,
            email = email,
            is_staff = is_staff,
            is_active = True,
            is_superuser = is_superuser,
            last_login = now,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, numero_documento, nombre_completo, password=None, **kwargs):
        """Funcion que realiza el registro de un usuario regular dentro del sistema"""
        return self._create_user(username, email, numero_documento, nombre_completo, password, False, False, **kwargs)
    
    def create_superuser(self, username, email, numero_documento, nombre_completo, password, **kwargs):
        """Funcion que realiza el registro de un usuario con privilegios de superusuario dentro del sistema"""
        return self._create_user(username, email, numero_documento, nombre_completo, password, True, True, **kwargs)


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Nombre de Usuario'), max_length=50, unique = True)
    email = models.CharField(_('Correo Electrónico'), max_length=50, null = True, blank = True)
    numero_documento = models.CharField(_('Nro. de Documento'), max_length = 25, unique = True)
    nombre_completo = models.CharField(_('Nombre Completo'), max_length = 150)
    cargo = models.CharField(_('Cargo'), max_length = 150, null = True, blank = True)
    cargo_id = models.IntegerField(_('Cargo ID'), null = True, blank = True)
    departamento = models.CharField(_('Departamento'), max_length = 15, null = True, blank = True)
    departamento_id = models.IntegerField(_('Departamento ID'), null = True, blank = True)
    is_active = models.BooleanField(_('Es Activo'), default = False)
    is_staff = models.BooleanField(_('Puede Logearse'), default = False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'numero_documento', 'nombre_completo']

    objects = UsuarioManager()