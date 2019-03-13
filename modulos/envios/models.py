from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model

from correos.utils.db import UpperCharField
from modulos.parametros.models import LogModel

Usuario = get_user_model()

class Pais (LogModel):
    nombre=models.CharField(_('Nombre de Pais'), max_length=50, blank=False, null=False)
    sigla=models.CharField(_('Sigla de Pais'), max_length=10, blank=False, null=False)
    codigo_postal=models.CharField(_('Còdigo Postal'), max_length=50, blank=True, null=True)
    codigo_pais=models.CharField(_('Còdigo de Pais'), max_length=50, blank=False, null=False)
    icono=models.CharField(_('Icono'), max_length=50, blank=False, null=False)
    
    def __str__(self):
        return self.nombre
    

class Departamento (LogModel):
    nombre=models.CharField(_('Nombre del departamento'), max_length=15, blank=False, null=False)
    detalle=models.CharField(_('Detalle del departamento'), max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre
    

class Ciudad (LogModel):
    nombre=models.CharField(_('Nombre de la Ciudad'), max_length=50, blank=False, null=False)
    departamento=models.ForeignKey(
        'Departamento',
        verbose_name=_('Departamento id'),
        related_name='+',
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.nombre


class Cargo (LogModel):
    nombre=models.CharField(_('Nombre del cargo'), max_length=50, blank=False, null=False)
    detalle=models.CharField(_('Detalle del cargo'), max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Oficina (LogModel):
    nombre=models.CharField(_('Nombre de la oficina'), max_length=50, blank=False, null=False)
    detalle=models.CharField(_('Detalle de la oficina'), max_length=100, blank=True, null=True)
    departamento_id=models.ForeignKey(
        'Departamento', 
        verbose_name=_('Departamento ID'),
        related_name='+',
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.nombre


class Envio (LogModel):
    """12 campos remitente"""
    documento_identidad_rem=models.CharField(_('Documento Identidad Remitente'), max_length=15, blank=True, null=True)
    fec_nac_rem=models.DateField(_('Fecha de Nacimiento'))
    documento_extrangero_rem=models.CharField(_('Documento de Extranjero'), max_length=15, blank=True, null=True)
    nombre_rem=models.CharField(_('Nombre del remitente'), max_length=50, blank=True, null=True)
    apellido_rem=models.CharField(_('Apellido del remitente'), max_length=50, blank=True, null=True)
    empresa_rem=models.CharField(_('Nombre de la empresa'), max_length=50, blank=True, null=True)
    pais_rem_id=models.ForeignKey(
        'Pais',
        verbose_name=_('Pais ID Remitente'),
        related_name='+',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    departamento_rem_id=models.ForeignKey(
        'Departamento',
        verbose_name=_('Departamento ID Remintente'),
        related_name='+',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    ciudad_rem=models.ForeignKey(
        'Ciudad',
        verbose_name=_('Ciudad Remitente'),
        related_name='+',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    direccion_rem=models.CharField(_('Direccion del remitente'), max_length=80, blank=True, null=True)
    direccion2_rem=models.CharField(_('Direccion 2 del remitente'), max_length=80, blank=True, null=True)
    direccion3_rem=models.CharField(_('Direccion 3 del remitente'), max_length=80, blank=True, null=True)
    codigo_postal_rem=models.CharField(_('Codigo Postal remitente'),max_length=10, blank=True, null=True)
    email_rem=models.CharField(_('Correo electronico del remitente'), max_length=50, blank=True, null=True)
    tipo_tel_rem=models.CharField(_('tipo de telefono del remitente'), max_length=50, blank=True, null=True)
    codigo_pais_rem=models.CharField(_('Codigo Pais Remitente'), max_length=10, blank=True, null=True)
    telefono_rem=models.CharField(_('Telefono del remitente'), max_length=50, blank=True, null=True)
    extension_rem=models.CharField(_('Extension del remitente'), max_length=50, blank=True, null=True)

    nombre_des=models.CharField(_('Nombre del Destinatario'), max_length=50, blank=True, null=True)
    empresa_des=models.CharField(_('Nombre de la empresa del destinatario'), max_length=50, blank=True, null=True)
    pais_des_id=models.ForeignKey(
        'Pais',
        verbose_name=_('Pais ID Destinatario'),
        related_name='+',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    email_des=models.CharField(_('Correo electronico del destinatario'), max_length=50, blank=True, null=True)
    departamento_des_id=models.ForeignKey(
        'Departamento',
        verbose_name=_('Departamento ID Destinatario'),
        related_name='+',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    ciudad_des=models.ForeignKey(
        'Ciudad',
        verbose_name=_('Ciudad Destinatario'),
        related_name='+',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    direccion_des=models.CharField(_('Direccion del destinatario'), max_length=50, blank=True, null=True)
    direccion2_des=models.CharField(_('Direccion 2 del destinatario'), max_length=50, blank=True, null=True)
    codigo_postal_des=models.CharField(_('Codigo Postal destinatario'),max_length=10, blank=True, null=True)
    tipo_tel_des=models.CharField(_('Tipo de telefono del destinatario'), max_length=50, blank=True, null=True)
    codigo_pais=models.CharField(_('Codigo Pais Destinatario'), max_length=10, blank=True, null=True)
    telefono_des=models.CharField(_('Telefono del destinatario'), max_length=50, blank=True, null=True)
    notas_des=models.CharField(_('Notas u observaciones del destinatario'), max_length=100, blank=True, null=True)
    identificacioniva_des=models.CharField(_('Identificacion IVA Destinatario'), max_length=50, blank=True, null=True)
    tipoidentificacionfiscal_des=models.CharField(_('Tipo de Identificacion Fiscal'), max_length=50, blank=True, null=True)
    identificacionfiscal=models.CharField(_('Identificacion Fiscal CNPJ/CPF'), max_length=5, blank=True, null=True)
    identificacionierg=models.CharField(_('Identificacion IR/EG'), max_length=5, blank=True, null=True)
    adjunto=models.FileField(_('Adjunto Archivo'), max_length=100, upload_to='adjuntos/', blank=True, null=True)

    def __str__(self):
        return self.nombre_rem