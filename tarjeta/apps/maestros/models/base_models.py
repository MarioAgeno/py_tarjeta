# tarjeta\apps\maestros\models\base_models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
#from django.core.exceptions import ValidationError
from .base_gen_models import ModeloBaseGenerico
from entorno.constantes_base import ESTATUS_GEN

#from decimal import Decimal

class Numero(ModeloBaseGenerico):
    id_numero = models.AutoField(primary_key=True)
    cupon = models.IntegerField()

    def __str__(self):
        return str(self.cupon)

    class Meta:
        db_table = 'numero'
        verbose_name = ('Numero')
        verbose_name_plural = ('Numeros')
        ordering = ['id_numero']


class Actividad(ModeloBaseGenerico):
    id_actividad = models.AutoField(primary_key=True)
    estatus_actividad = models.BooleanField("Estatus", db_column="estatus", 
                                            default=True, choices=ESTATUS_GEN)    
    nombre_actividad = models.CharField('Nombre', db_column="nombre", max_length=30, blank=True)
    interes_actividad = models.DecimalField('Interes(%)', db_column="interes", 
                                            max_digits=6, decimal_places=2, 
                                            validators=[MinValueValidator(0), 
											            MaxValueValidator(100.00)])
    codigo_afip = models.IntegerField('Codigo de AFIP', db_column="afip", blank=True)

    def __str__(self):
        return self.nombre_actividad
    
    class Meta:
        db_table = 'actividad'
        verbose_name = ('Actividad')
        verbose_name_plural = ('Actividades')
        ordering = ['nombre_actividad']


class TipoIva(ModeloBaseGenerico):
    id_tipo_iva = models.AutoField(primary_key=True)
    estatus_tipo_iva = models.BooleanField("Estatus", db_column="estatus", 
                                           default=True, choices=ESTATUS_GEN)    
    codigo_iva = models.CharField("Codigo", db_column="codigo",  max_length=4)
    nombre_iva = models.CharField("Nombre", db_column="nombre", 
                                  max_length=20, blank=True)
    discrimina_iva = models.BooleanField(blank=True)

    def __str__(self):
        return self.nombre_iva

    class Meta:
        db_table = 'tipo_iva'
        verbose_name = ('Tipo de IVA')
        verbose_name_plural = ('Tipos de IVA')
        ordering = ['nombre_iva']


class TipoDocumentoIdentidad(ModeloBaseGenerico):
    id_tipo_documento_identidad = models.AutoField(primary_key=True)
    estatus_tipo_documento_identidad = models.BooleanField("Estatus", db_column="estatus", 
                                                           default=True, choices=ESTATUS_GEN)
    tipo_documento_identidad = models.CharField(max_length=4, db_column="tipo")
    descripcion_documento_identidad = models.CharField(max_length=25, db_column="descripcion")
    codigo_afip = models.CharField(max_length=2, db_column="codigo_afip")

    def __str__(self):
        return self.tipo_documento_identidad
    
    class Meta:
        db_table = 'tipo_documento_identidad'
        verbose_name = ('Tipo de Documento de Identidad')
        verbose_name_plural = ('Tipos de Documentos de Identidad')
        ordering = ['tipo_documento_identidad']


class TarjetaEstado(ModeloBaseGenerico):
    id_tarjeta_estado = models.AutoField(primary_key=True)
    estatus_tarjeta_estado = models.BooleanField("Estatus", db_column="estatus", 
                                                 default=True, choices=ESTATUS_GEN)
    descripcion_tarjeta_estado = models.CharField(max_length=30, blank=True, 
                                                  db_column="descripcion")
    mensaje = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.descripcion_tarjeta_estado
    
    class Meta:
        db_table = 'tarjeta_estado'
        verbose_name = ('Estado Tarjeta')
        verbose_name_plural = ('Estados Tarjetas')
        ordering = ['descripcion_tarjeta_estado']


class Plan(ModeloBaseGenerico):
    id_plan = models.AutoField(primary_key=True)
    estatus_plan = models.BooleanField("Estatus", db_column="estatus", 
                                       default=True, choices=ESTATUS_GEN)
    nombre_plan = models.CharField("Nombre", max_length=30, db_column="nombre")
    cuotas_plan = models.IntegerField("Cuotas*", db_column="cuotas")
    interes_plan = models.DecimalField("Interes(%)", db_column="interes", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    costo_financiero_plan = models.DecimalField("Costo Financiero(%)", db_column="costo_financiero", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    vencimiento_plan = models.DateTimeField(db_column="vencimiento")
    
    def __str__(self):
        return self.nombre_plan
    
    class Meta:
        db_table = 'plan'
        verbose_name = ('Plan de Financiacion')
        verbose_name_plural = ('Planes de Financiacion')
        ordering = ['nombre_plan']


class Titulo(ModeloBaseGenerico):
    id_titulo = models.AutoField(primary_key=True)
    estatus_titulo = models.BooleanField("Estatus", db_column="estatus", 
                                         default=True, choices=ESTATUS_GEN)
    titulo = models.CharField("Nombre*", max_length=30, blank=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'titulo'
        verbose_name = ('Titulo')
        verbose_name_plural = ('Titulos')
        ordering = ['titulo']


class Sucursal(ModeloBaseGenerico):
    id_sucursal = models.AutoField(primary_key=True)
    estatus_sucursal = models.BooleanField("Estatus", db_column="estatus", default=True, choices=ESTATUS_GEN)
    nombre_sucursal = models.CharField("Nombre", db_column="nombre", max_length=30, blank=True)
    domicilio_sucursal = models.CharField("Domicilio", db_column="domicilio", max_length=30, blank=True)
    localidad_sucursal = models.CharField("Localidad", db_column="localidad", max_length=30, blank=True)
    codigo_postal = models.CharField("Codigo Postal", max_length=10, blank=True)
    telefono = models.CharField("Telefono", max_length=15, blank=True)
    telefono2 = models.CharField("Telefono", max_length=15, blank=True)
    movil = models.CharField("Movil", max_length=30, blank=True)
    mail = models.EmailField("eMail", max_length=40, blank=True)
    ruta_archivo = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre_sucursal
    
    class Meta:
        db_table = 'sucursal'
        verbose_name = ('Sucursal')
        verbose_name_plural = ('Sucursales')
        ordering = ['nombre_sucursal']


class Empresa(ModeloBaseGenerico):
    id_empresa = models.AutoField(primary_key=True)
    estatus_empresa = models.BooleanField("Estatus", db_column="estatus",
                                           default=True, choices=ESTATUS_GEN)
    razon_social = models.CharField("Razon Social", max_length=50, blank=True)
    nombre_empresa = models.CharField("Nombre", db_column="nombre", max_length=50, blank=True)
    domicilio = models.CharField("Domicilio", max_length=30, blank=True)
    localidad = models.CharField("Localidad", max_length=20, blank=True)
    provincia = models.CharField("Provincia", max_length=20, blank=True)
    codigo_postal = models.CharField("Codigo Postal", max_length=8, blank=True)
    iva = models.CharField("IVA", max_length=15, blank=True)
    cuit = models.CharField("CUIT", max_length=13, blank=True)
    ingreso_bruto = models.CharField("Ingresos Brutos", max_length=11, blank=True)
    telefono = models.CharField("Telefono", max_length=15, blank=True)
    telefono2 = models.CharField("Telefono", max_length=15, blank=True)
    movil = models.CharField("Movil", max_length=15, blank=True)
    mail = models.EmailField("eMail", max_length=50, blank=True)
    web = models.CharField("URL WEB", max_length=50, blank=True)
    imagen = models.CharField("Logo", max_length=50, blank=True)

    def __str__(self):
        return self.nombre_empresa
    
    class Meta:
        db_table = 'empresa'
        verbose_name = ('Empresa')
        verbose_name_plural = ('Empresas')
        ordering = ['nombre_empresa']


class Parametro(ModeloBaseGenerico):
    id_parametro = models.AutoField(primary_key=True)
    gastos = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    tasa = models.DecimalField("Tasa Mora(%)", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    punitorios = models.DecimalField("Interes Punitorio(%)", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    minimo = models.DecimalField("Pago Minimo(%)", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    cierre_ultimo = models.DateTimeField(blank=True)
    cierre_actual = models.DateTimeField(blank=True)
    cierre_proximo = models.DateTimeField(blank=True)
    vencimiento_ultimo = models.DateTimeField(blank=True)
    vencimiento_actual = models.DateTimeField(blank=True)
    vencimiento_proximo = models.DateTimeField(blank=True)
    retencion_debito_credito = models.DecimalField("Retencion DB/CD(%)", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    retencion_ib_general = models.DecimalField("Renecion IIBB General(%)", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    retencion_ib = models.DecimalField("Retencion IIBB(%)", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    retencion_ib_minimo = models.DecimalField("Minimo Retencion IIBB", max_digits=14, decimal_places=2, 
							 validators=[MinValueValidator(0), 
										 MaxValueValidator(9999999999999.99)])
    retencion_ganancia = models.DecimalField("Retencion Ganancias(%)", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    retencion_ganancia_nc = models.DecimalField("Retencion Ganancias NC(%)", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    retencion_ganancia_minimo = models.DecimalField("Minimo Retencion Ganancias", max_digits=15, decimal_places=2, 
							 validators=[MinValueValidator(0), 
										 MaxValueValidator(9999999999999.99)])
    retencion_ganancia_minimo_nc = models.DecimalField("Minimo Retencion Ganancias NC", max_digits=15, decimal_places=2, 
							 validators=[MinValueValidator(0), 
										 MaxValueValidator(9999999999999.99)])
    retencion_iva = models.DecimalField("Retencion IVA(%)", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    retencion_iva_estacion_servicio = models.DecimalField("Retencion IVA Est.Servicios(%)", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    retencion_iva_nc = models.DecimalField("Retencion IVA NC(%)", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    retencion_iva_minimo = models.DecimalField("Minimo Retencion IVA", max_digits=15, decimal_places=2, 
							 validators=[MinValueValidator(0), 
										 MaxValueValidator(9999999999999.99)])
    sello = models.DecimalField("Sellado(%)", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    seguro = models.DecimalField("Seguro Vida(%)", max_digits=4, decimal_places=2, 
								validators=[MinValueValidator(0), 
											MaxValueValidator(100.00)])
    dias_mora = models.DecimalField(max_digits=2, decimal_places=0, blank=True)
    mensaje = models.CharField(max_length=250, blank=True)
    gastos_mail = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    codigo_roela = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.id_parametro)
    
    class Meta:
        db_table = 'parametro'
        verbose_name = ('Parametro')
        verbose_name_plural = ('Parametros')
        ordering = ['id_parametro']


class Provincia(ModeloBaseGenerico):
	id_provincia = models.AutoField(primary_key=True)
	estatus_provincia = models.BooleanField("Estatus", db_column="estatus", default=True,
											choices=ESTATUS_GEN)
	codigo_provincia = models.CharField("Código", db_column="codigo", max_length=1)
	nombre_provincia = models.CharField("Nombre", db_column="nombre", max_length=30)

	def __str__(self):
		return self.nombre_provincia

	class Meta:
		db_table = 'provincia'
		verbose_name = ('Provincia')
		verbose_name_plural = ('Provincias')
		ordering = ['nombre_provincia']


class Localidad(ModeloBaseGenerico):
	id_localidad = models.AutoField(primary_key=True)
	estatus_localidad = models.BooleanField("Estatus", db_column="estatus", default=True,
											choices=ESTATUS_GEN)
	nombre_localidad = models.CharField("Nombre Localidad", db_column="nombre", max_length=30)
	codigo_postal = models.CharField("Código Postal", max_length=5)
	id_provincia = models.ForeignKey('Provincia', on_delete=models.CASCADE,
									 verbose_name="Provincia")

	def __str__(self):
		return self.nombre_localidad

	class Meta:
		db_table = 'localidad'
		verbose_name = ('Localidad')
		verbose_name_plural = ('Localidades')
		ordering = ['codigo_postal']

