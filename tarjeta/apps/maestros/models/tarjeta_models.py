# tarjeta\apps\maestros\models\tarjeta_models.py
from django.db import models
from django.core.exceptions import ValidationError
import re
from .base_gen_models import ModeloBaseGenerico
from .base_models import (Actividad, Sucursal, Localidad, Provincia, 
						  TipoDocumentoIdentidad, Titulo, TarjetaEstado)
from entorno.constantes_base import (SEGURO,
	ESTATUS_GEN, PEP, TIPO_PERSONA)


class Socio(ModeloBaseGenerico):
    id_socio = models.AutoField(primary_key=True)
    estatus_socio = models.BooleanField("Estatus*", default=True, choices=ESTATUS_GEN)
    id_sucursal_socio = models.ForeignKey(Sucursal, on_delete=models.PROTECT, 
                                          verbose_name="Sucursal*")
    codigo_socio = models.IntegerField()
    nombre_socio = models.CharField(max_length=40)
    domicilio_socio = models.CharField(max_length=30, blank=True)
    id_localidad_socio = models.ForeignKey(Localidad, on_delete=models.PROTECT, 
                                           verbose_name="Localidad*")
    id_provincia_socio = models.ForeignKey(Provincia, on_delete=models.PROTECT, 
                                           verbose_name="Provincia*")
    telefono_socio = models.CharField(max_length=15, blank=True)
    telefono2_socio = models.CharField(max_length=15, blank=True)
    movil_socio = models.EmailField(max_length=15, blank=True)
    mail_socio = models.EmailField(max_length=50, blank=True)
    id_tipo_documento_identidad = models.ForeignKey(TipoDocumentoIdentidad, 
                                                    on_delete=models.PROTECT, verbose_name="Documento*")
    numero_documento = models.DecimalField(max_digits=9, decimal_places=0, blank=True)
    fecha_nacimiento = models.DateTimeField(blank=True)
    cuit_socio = models.DecimalField(max_digits=11, decimal_places=0, blank=True)
    nacionalidad = models.CharField(max_length=20, blank=True)
    id_actividad = models.ForeignKey(Actividad, on_delete=models.PROTECT, 
                                     verbose_name="Actividad*")
    tipo_persona = models.CharField("Tipo de Persona*", max_length=1, default="F", choices=TIPO_PERSONA)
    pep = models.BooleanField("PEPs*", default=True, choices=PEP)
    fecha_ingreso = models.DateField(blank=True)

    def __str__(self):
        return self.nombre_socio
    
    class Meta:
        db_table = 'socio'
        verbose_name = ('Socio')
        verbose_name_plural = ('Socios')
        ordering = ['nombre_socio']


class Tarjeta(ModeloBaseGenerico):
    id_tarjeta = models.AutoField(primary_key=True)
    estatus_tarjeta = models.BooleanField("Estatus*", default=True, choices=ESTATUS_GEN)
    id_sucursal_tarjeta = models.ForeignKey(Sucursal, on_delete=models.PROTECT, 
                                            verbose_name="Sucursal*")
    id_socio = models.ForeignKey(Socio, on_delete=models.PROTECT, verbose_name="Socio*")
    adicional = models.IntegerField(blank=True)
    digito_verificador = models.IntegerField(blank=True)
    nombre_titular = models.CharField(max_length=40, blank=True)
    domicilio = models.CharField(max_length=40, blank=True)
    id_localidad_tarjeta = models.ForeignKey(Localidad, on_delete=models.PROTECT, 
                                           verbose_name="Localidad*")
    id_provincia_tarjeta = models.ForeignKey(Provincia, on_delete=models.PROTECT, 
                                           verbose_name="Provincia*")
    telefono_tarjeta = models.CharField(max_length=15, blank=True)
    telefono2_tarjeta = models.CharField(max_length=15, blank=True)
    movil_tarjeta = models.CharField(max_length=15, blank=True)
    mail_tarjeta = models.EmailField(max_length=50, blank=True)
    nombre_garantia = models.CharField(max_length=40, blank=True)
    limite_maximo_tarjeta = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    saldo_disponible = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    id_titulo = models.ForeignKey(Titulo, on_delete=models.PROTECT, verbose_name="Titulo*")
    id_tarjeta_estado = models.ForeignKey(TarjetaEstado, on_delete=models.PROTECT, 
                                          verbose_name="Estado*")
    fecha_alta = models.DateTimeField(blank=True)
    fecha_baja = models.DateTimeField(blank=True)
    vencimiento = models.DateTimeField(blank=True)
    liquidacion_mail = models.BooleanField(blank=True)
    seguro = models.BooleanField("Seguro*", default=True, choices=SEGURO)
    observacion = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre_titular
    
    class Meta:
        db_table = 'tarjeta'
        verbose_name = ('Tarjeta')
        verbose_name_plural = ('Tarjetas')
        ordering = ['nombre_titular']


class RegitroLimite(ModeloBaseGenerico):
    id_registro_limite = models.AutoField(primary_key=True)
    estatus_registro_limite = models.BooleanField("Estatus", default=True, choices=ESTATUS_GEN)
    id_tarjeta = models.ForeignKey(Tarjeta, on_delete=models.PROTECT, verbose_name="Tarjeta*")
    fecha_limite = models.DateTimeField()
    maximo_limite = models.DecimalField(max_digits=14, decimal_places=2)

    def __str__(self):
        return self.id_tarjeta
    
    class Meta:
        db_table = 'registro_limite'
        verbose_name = ('Registro Limite')
        verbose_name_plural = ('Registro de Limites')
        ordering = ['id_tarjeta']
