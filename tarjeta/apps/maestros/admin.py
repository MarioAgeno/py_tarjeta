from django.contrib import admin

# Register your models here.

from .models.base_models import *
from .models.comercio_models import *
from .models.tarjeta_models import *
from .models.liquidacion_models import *

# Registramos los modelos independientes

# Registramos los modelos base
admin.site.register(Actividad)
admin.site.register(Localidad)
admin.site.register(Provincia)
admin.site.register(TipoDocumentoIdentidad)
admin.site.register(TipoIva)
admin.site.register(Sucursal)
admin.site.register(Plan)
admin.site.register(Empresa)
admin.site.register(Numero)
admin.site.register(Parametro)
admin.site.register(TarjetaEstado)
admin.site.register(Titulo)
admin.site.register(PlanComercio)
admin.site.register(Comercio)
admin.site.register(Tarjeta)
admin.site.register(RegitroLimite)
admin.site.register(LiquidacionSocio)

