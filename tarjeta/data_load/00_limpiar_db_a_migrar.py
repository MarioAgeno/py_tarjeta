# Migrar tabla cuota al modelos DJango

import os
import sys
import django
from django.db import connection

# Agrega la ruta base del proyecto y la ruta interna del settings al PATH
sys.path.append("D:/Python/PROYECTO_TARJETA/tarjeta")

# Configura el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tarjeta.settings")
django.setup()

#import pyodbc
from django.db import transaction
from apps.maestros.models.base_models import *
from apps.maestros.models.comercio_models import *
from apps.maestros.models.compra_models import *
from apps.maestros.models.liquidacion_models import *
from apps.maestros.models.tarjeta_models import *

def reset_modelo():
    # Elimina todos los registros del modelo `cuota` en Django
    Cuota.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='cuota'")

    # Elimina todos los registros del modelo `liquidacion_socio` en Django
    LiquidacionSocio.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='liquidacion_socio'")

        # Elimina todos los registros del modelo `Operacion` en Django
    Operacion.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='operacion'")

    # Elimina todos los registros del modelo `compra` en Django
    Compra.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='compra'")

    # Elimina todos los registros del modelo `registro_limite` en Django
    RegitroLimite.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='registro_limite'")

    # Elimina todos los registros del modelo `tarjeta` en Django
    Tarjeta.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='tarjeta'")

    # Elimina todos los registros del modelo `liquidacion_comercio` en Django
    LiqudacionComercio.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='liquidacion_comercio'")

    # Elimina todos los registros del modelo `Plan_comercio` en Django
    PlanComercio.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='plan_comercio'")

    # Elimina todos los registros del modelo `Comercio` en Django
    Comercio.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='comercio'")

    # Elimina todos los registros del modelo `parametros` en Django
    Parametro.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='parametro'")

    # Elimina todos los registros del modelo `Empresa` en Django
    Empresa.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='empresa'")


    # Elimina todos los registros del modelo `sucursal` en Django
    Sucursal.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='sucursal'")


    # Elimina todos los registros del modelo `Titulo` en Django
    Titulo.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='titulo'")

    # Elimina todos los registros del modelo `plan` en Django
    Plan.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='plan'")

    # Elimina todos los registros del modelo `tarjeta_estado` en Django
    TarjetaEstado.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='tarjeta_estado'")

    # Elimina todos los registros del modelo `tipo_documento_identidad ` en Django
    TipoDocumentoIdentidad.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='tipo_documento_identidad'")

    # Elimina todos los registros del modelo `tipo_iva` en Django
    TipoIva.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='tipo_iva'")

    # Elimina todos los registros del modelo `Actividad` en Django
    Actividad.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='actividad'")

    # Elimina todos los registros del modelo `numero` en Django
    Numero.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='numero'")
        
reset_modelo()  # Eliminar datos existentes antes de migrar
