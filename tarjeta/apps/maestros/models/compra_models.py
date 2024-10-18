# tarjeta\apps\maestros\models\compra_models.py
from django.db import models
from .base_gen_models import ModeloBaseGenerico
from .base_models import Plan
from .comercio_models import Comercio
from .tarjeta_models import Tarjeta

class Compra(ModeloBaseGenerico):
    id_compra = models.AutoField(primary_key=True)
    cupon_compra = models.IntegerField("Cupon", db_column="cupon")
    fecha_compra = models.DateTimeField("Fecha", db_column="fecha", blank=True)
    id_comercio = models.ForeignKey(Comercio, on_delete=models.PROTECT, verbose_name="Comercio*")
    id_tarjeta = models.ForeignKey(Tarjeta, on_delete=models.PROTECT, verbose_name="Tarjeta*")
    importe_compra = models.DecimalField("Importe" , db_column="importe", max_digits=10, decimal_places=2)
    id_plan = models.ForeignKey(Plan, on_delete=models.PROTECT, verbose_name="Plan*")
    autorizacion = models.IntegerField("Autorizacion", db_column="autorizacion")
    procesada = models.BooleanField("Procesada", db_column="procesada")
    tipo_carga = models.CharField("Tipo Carga", max_length=1, blank=True)
    whatsapp = models.BigIntegerField()

    def __str__(self):
        return self.id_comercio
    
    class Meta:
        db_table = 'compra'
        verbose_name = ('Compra')
        verbose_name_plural = ('Compras')
        ordering = ['fecha_compra']

class Operacion(ModeloBaseGenerico):
    id_operacion = models.AutoField(primary_key=True)
    cupon_operacion = models.IntegerField("Cupon", db_column="cupon")
    fecha_operacion = models.DateTimeField("Fecha", db_column="fecha")
    id_comercio = models.ForeignKey(Comercio, on_delete=models.PROTECT, verbose_name="Comercio*")
    id_tarjeta = models.ForeignKey(Tarjeta, on_delete=models.PROTECT, verbose_name="Tarjeta*")
    importe_compra = models.DecimalField("Importe", db_column="importe", max_digits=10, decimal_places=2)
    id_plan = models.ForeignKey(Plan, on_delete=models.PROTECT, verbose_name="Plan*")
    autorizacion = models.IntegerField("Autorizacion", db_column="autorizacion")
    acreditado = models.DateTimeField(blank=True)
    liquidacion_comercio = models.IntegerField("Liquidacion Comercio", db_column="liquidacion_comercio", blank=True)
    estado_operacion = models.CharField(max_length=1, blank=True)
    tipo_carga = models.CharField("Tipo Carga", max_length=1, blank=True)

    def __str__(self):
        return self.id_comercio
    
    class Meta:
        db_table = 'operacion'
        verbose_name = ('Operacion')
        verbose_name_plural = ('Operaciones')
        ordering = ['fecha_compra']