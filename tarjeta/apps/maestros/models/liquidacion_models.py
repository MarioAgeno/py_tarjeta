# proyecto_tarjeta\apps\maestros\models\liquidacion_models.py
from django.db import models
#from django.core.exceptions import ValidationError
#import re
from .base_gen_models import ModeloBaseGenerico
from .tarjeta_models import Tarjeta
from .compra_models import Operacion
from entorno.constantes_base import (
	ESTATUS_GEN, CONDICION_VENTA, SEXO, 
	TIPO_PERSONA, BLACK_LIST)

class LiquidacionSocio(ModeloBaseGenerico):
    id_liquidacion_socio = models.AutoField(primary_key=True)
    id_tarjeta = models.ForeignKey(Tarjeta, on_delete=models.PROTECT, verbose_name="Tarjeta*")
    numero_tarjeta = models.BigIntegerField()
    comprobante = models.CharField("Comprobante", max_length=2, blank=True)
    liquidacion_socio = models.IntegerField("Numero Liquidacion", db_column="liquidacion", blank=True)
    cierre_anterior = models.DateField("Cierre Anterior", blank=True)
    cierre_actual = models.DateField("Cierre Actual", blank=True)
    cierre_proximo = models.DateField("Proximo Cierre", blank=True)
    vencimiento_anterior = models.DateField("Vencimiento Anterior", blank=True)
    vencimiento = models.DateField("Vencimiento", blank=True)
    vencimiento_proximo = models.DateField("Proximo Vencimiento", blank=True)
    limite_tarjeta = models.DecimalField("Limite Tarjeta", max_digits=10, decimal_places=2, blank=True)
    saldo_anterior = models.DecimalField("Saldo Anterior", max_digits=10, decimal_places=2, blank=True)
    pago_anterior = models.DecimalField("Pago Anterior", max_digits=10, decimal_places=2, blank=True)
    importe_liquidacion = models.DecimalField("Importe", db_column="importe", max_digits=10, decimal_places=2, blank=True)
    pago_minimo = models.DecimalField("Pago Minimo", db_column="minimo", max_digits=10, decimal_places=2, blank=True)
    importe_seguro = models.DecimalField("Seguro", db_column="seguro", max_digits=10, decimal_places=2, blank=True)
    importe_gasto = models.DecimalField("Gastos", db_column="gastos", max_digits=10, decimal_places=2, blank=True)
    importe_interes = models.DecimalField("Interes", db_column="interes", max_digits=10, decimal_places=2, blank=True)
    importe_punitorio = models.DecimalField("Punitorios", db_column="punitorio", max_digits=10, decimal_places=2, blank=True)
    importe_sellado = models.DecimalField("Sellado", db_column="sellado", max_digits=10, decimal_places=2, blank=True)
    importe_total = models.DecimalField("Importe Total", db_column="total", max_digits=10, decimal_places=2, blank=True)
    su_pago = models.DecimalField("Su Pago", max_digits=10, decimal_places=2, blank=True)
    fecha_pago = models.DateTimeField("Fecha Pago", blank=True)
    sucursal_pago = models.IntegerField("Sucursal Pago", blank=True)

    def __str__(self):
        return self.id_tarjeta
    
    class Meta:
        db_table = 'liquidacion_socio'
        verbose_name = ('Liquidacio Socio')
        verbose_name_plural = ('Liquidaciones de Socios')
        ordering = ['liquidacion_socio']


class Cuota(ModeloBaseGenerico):
    id_cuota = models.AutoField(primary_key=True)
    id_compra = models.ForeignKey(Operacion, on_delete=models.PROTECT, verbose_name="Compra*")
    numero_cuota = models.IntegerField("Numero", db_column="numero")
    vencimiento_cuota = models.DateField("Vencimiento", db_column="vencimiento")
    capital_cuota = models.DecimalField("Capital", db_column="capital", max_digits=10, decimal_places=2)
    interes_cuota = models.DecimalField("Interes", db_column="interes", max_digits=10, decimal_places=2)
    importe_cuota = models.DecimalField("Importe Cuota", db_column="importe", max_digits=10, decimal_places=2)
    liquidacion_socio = models.IntegerField("Numero Liquidacion", db_column="liquidacion", blank=True)

    def __str__(self):
        return self.id_compra
    
    class Meta:
        db_table = 'cuota'
        verbose_name = ('Cuota')
        verbose_name_plural = ('Cuotas')
        ordering = ['id_compra']

