from django.contrib import admin

# Register your models here.

from .models.base_models import *

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

