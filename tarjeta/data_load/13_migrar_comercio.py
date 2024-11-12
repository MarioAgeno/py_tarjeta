# Migrar tabla Comercio al  modelos DJango

import os
import sys
import django
from django.db import connection

# Agrega la ruta base del proyecto y la ruta interna del settings al PATH
sys.path.append("D:/Python/PROYECTO_TARJETA/tarjeta")

# Configura el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tarjeta.settings")
django.setup()

import pyodbc
from django.db import transaction
from apps.maestros.models.comercio_models import Comercio

# Conexión a la base de datos SQL Server
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=PCMARIO\SQLEXPRESS;DATABASE=Tarjetas;UID=sa;PWD=maasoft')
cursor = conn.cursor()

# Query para obtener los datos de la tabla SQL Server
cursor.execute("SELECT * FROM tjComercios")

def reset_modelo():
    # Elimina todos los registros del modelo `Comercio` en Django
    Comercio.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='comercio'")


# Transacción para insertar los datos de titulos en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    for row in cursor.fetchall():
        # Depuración: imprime el contenido de la fila para verificar los datos
        print(row)  # Esto imprimirá cada fila obtenida de SQL Server

        # Ajusta estos nombres de campo para que coincidan con tu modelo `Titulo` y la consulta SQL
        Comercio.objects.create(
            estatus_comercio=True,
            codigo_comercio=row[1],
            pin=row[2],
            razon_social_comercio=row[3],
            nombre_titular=row[4],
            domicilio_comercio=row[5],
            id_localidad_comercio=row[6],
            id_provincia_comercio=row[7],
            telefono_comercio=row[8],
            telefono2_comercio=row[9],
            movil_comercio=row[10],
            mail_comercio=row[11],
            id_actividad=row[12],
            id_sucursal_comercio=row[13],
            codigo_socio=row[14],
            id_iva_comercio=row[15],
            cuit_comercio=row[16],
            ingreso_bruto=row[17],
            monto_fijo=row[18],
            estacion_servicio=row[19],
            debito_credito=row[20],
            acreditar_cuenta=row[21],
            exento_ganancias=row[22],
            mensaje=row[23],
            leido=row[24],
            porcentaje_consumo=row[25],
            porcentaje_retencion_ib=row[26]
        )


# Cerrar la conexión
conn.close()
