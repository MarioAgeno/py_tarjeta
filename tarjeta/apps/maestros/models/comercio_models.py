# tarjeta\apps\maestros\models\comercio_models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
import re
from .base_gen_models import ModeloBaseGenerico
from .base_models import (Plan, Actividad, Sucursal, Localidad, Provincia, TipoIva)
from utils.validatos.validaciones import validar_cuit
from entorno.constantes_base import ESTATUS_GEN


class Comercio(ModeloBaseGenerico):
    id_comercio = models.AutoField(primary_key=True)
    estatus_comercio = models.BooleanField("Estatus*", db_column="estatus", default=True, choices=ESTATUS_GEN)
    codigo_comercio = models.IntegerField("Codigo*", db_column="codigo", unique=True)
    pin = models.IntegerField()
    razon_social_comercio = models.CharField("Razon Social*", db_column="razon_social", max_length=40)
    nombre_titular = models.CharField("Titular*", db_column="titular", max_length=40)
    domicilio_comercio = models.CharField("Domicilio", db_column="domicilio", max_length=40)
    id_localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, 
                                              verbose_name="Localidad*", db_column="id_localidad")
    id_provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, 
                                              verbose_name="Provincia*", db_column="id_provincia")
    telefono_comercio = models.CharField("Telefono*", db_column="telefono", max_length=15)
    telefono2_comercio = models.CharField("Telefono 2", db_column="telefono2", max_length=15, blank=True)
    movil_comercio = models.CharField("Movil*", db_column="movil", max_length=15)
    mail_comercio = models.EmailField("eMail", db_column="mail", max_length=50, blank=True)
    id_actividad = models.ForeignKey(Actividad, on_delete=models.PROTECT, 
                                     verbose_name="Actividad*")
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT, 
                                             verbose_name="Sucursal*", db_column="id_sucursal")
    codigo_socio = models.IntegerField("Codigo Socio", default=0)
    id_tipo_iva = models.ForeignKey(TipoIva, on_delete=models.PROTECT, default=1, 
                                        verbose_name="IVA*", db_column="id_tipo_iva")
    cuit_comercio = models.DecimalField("CUIT*", db_column="cuit", max_digits=11, decimal_places=0)
    ingreso_bruto = models.CharField("Ingresos Brutos", max_length=15, blank=True)
    monto_fijo = models.BooleanField("Monto Fijo", blank=True)
    estacion_servicio = models.BooleanField("Estacion de servicios", blank=True)
    debito_credito = models.BooleanField("Debito/Credito", blank=True)
    acreditar_cuenta = models.BooleanField("Acredita en Cuenta", blank=True)
    exento_ganancias = models.BooleanField("Exento Ganancias", blank=True)
    mensaje = models.CharField("Mensaje", max_length=120, blank=True)
    leido = models.BooleanField("Leido", blank=True)
    porcentaje_consumo = models.DecimalField("Cosumo(%)", db_column="consumo", max_digits=5, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    porcentaje_retencion_ib = models.DecimalField("Rentecion IIBB(%)", db_column="retencion_ib", max_digits=5, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)]) 

    def __str__(self):
        return self.razon_social_comercio

    def clean(self):
        super().clean()
		
        errors = {}
		
        telefono_str = str(self.telefono_comercio) if self.telefono_comercio else ''
        movil_comercio_str = str(self.movil_comercio) if self.movil_comercio else ''
		
        try:
            validar_cuit(self.cuit_comercio)
        except ValidationError as e:
            errors['cuit_comercio'] = e.messages
		
        if not re.match(r'^\+?\d[\d ]{0,14}$', telefono_str):
            errors.update({'telefono_comercio': 'Debe indicar sólo dígitos numéricos positivos, mínimo 1 y máximo 15, el signo + y espacios.'})
		
        if movil_comercio_str and not re.match(r'^\+?\d[\d ]{0,14}$', movil_comercio_str):
            errors.update({'movil_comercio': 'Debe indicar sólo dígitos numéricos positivos, mínimo 1 y máximo 15, el signo +, espacios o vacío.'})
		
        if errors:
            raise ValidationError(errors)


    class Meta:
        db_table = 'comercio'
        verbose_name = ('Comercio')
        verbose_name_plural = ('Comercios')
        ordering = ['razon_social_comercio']


class LiquidacionComercio(ModeloBaseGenerico):
    id_liquidacion_comercio = models.AutoField(primary_key=True)
    liquidacion_comercio = models.IntegerField("Numero Liquidacion", db_column="liquidacion")
    id_comercio = models.ForeignKey(Comercio, on_delete=models.PROTECT, verbose_name="Comercio*")
    fecha_liquidacion = models.DateField("Fecha", db_column="fecha")
    importe_liquidacion = models.DecimalField("Importe Liquidacion", db_column="importe", max_digits=14, decimal_places=2)
    importe_comision = models.DecimalField("Comision", db_column="comision", max_digits=14, decimal_places=2)
    costo_financiero = models.DecimalField("Costo Financiero", max_digits=10, decimal_places=2)
    retencion_ganancias = models.DecimalField("Retencion Ganancias", max_digits=14, decimal_places=2, blank=True)
    retencion_iva = models.DecimalField("Retencion IVA", max_digits=14, decimal_places=2, blank=True)
    retencio_ib = models.DecimalField("Retencion IIBB", max_digits=14, decimal_places=2, blank=True)
    retencion_debito_credito = models.DecimalField("Retencion DB/CD", max_digits=14, decimal_places=2, blank=True)
    total_liquidacion = models.DecimalField("Total", db_column="total", max_digits=14, decimal_places=2, blank=True)

    def __str__(self):
        return f"Liquidación {self.id_liquidacion_comercio} - Comercio: {self.id_comercio.razon_social_comercio}"

    class Meta:
        db_table = 'liquidacion_comercio'
        verbose_name = ('Liquidacio Comercio')
        verbose_name_plural = ('Liquidaciones a Comercios')
        ordering = ['liquidacion_comercio']


class PlanComercio(ModeloBaseGenerico):
    id_plan_comercio = models.AutoField(primary_key=True)
    estatus_plan_comercio = models.BooleanField("Estatus*", db_column="estatus", default=True, choices=ESTATUS_GEN)
    id_plan = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name="Plan*")
    id_comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE, verbose_name="Comercio*")

    def __str__(self):
        return str(self.id_plan.nombre_plan)
    
    class Meta:
        db_table = 'plan_comercio'
        verbose_name = ('Plan Comercio')
        verbose_name_plural = ('Planes de Comercios')
        ordering = ['id_plan']

