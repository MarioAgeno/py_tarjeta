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
from apps.maestros.models.base_models import Localidad, Provincia, Actividad, Sucursal, TipoIva

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
        # print(row[0], row[2])  # Esto imprimirá cada fila obtenida de SQL Server

        # Filtra las localidades por código postal y selecciona los campos 'id_localidad' y 'id_provincia_id'
        cp = row[7].strip()
        localidad = Localidad.objects.filter(codigo_postal=cp).first()
        provincia = Provincia.objects.get(id_provincia=localidad.id_provincia_id)
        actividad = Actividad.objects.get(id_actividad=row[12])
        sucursal = Sucursal.objects.get(id_sucursal=row[13])
        tipo_iva = TipoIva.objects.filter(codigo_iva=row[15]).first()

        # Verifica si se encontró una localidad con el código postal dado 
        if not localidad: 
            print(f"No se encontró una localidad para el código postal: {row[7]} para {row[0]} {row[2]}")
            continue

        if not provincia: 
            print(f"No se encontró una Provincia para el codigo postal: {row[7]} para {row[0]} {row[2]}")
            continue

        if not actividad: 
            print(f"No se encontró una Activodad para el codigo postal: {row[12]} para {row[0]} {row[2]}")
            continue

        if not tipo_iva:
            print(f"No se encontró un Codigo de IVA para: {row[15]} para {row[0]} {row[2]}")
            continue

        if not sucursal:
            print(f"No se encontró la Sucursal: {row[13]} para {row[0]} {row[2]}")
            continue

        # Ajusta estos nombres de campo para que coincidan con tu modelo `Titulo` y la consulta SQL
        Comercio.objects.create(
            estatus_comercio=True,
            codigo_comercio=row[0],
            pin=row[1],
            razon_social_comercio=row[2],
            nombre_titular=row[3],
            domicilio_comercio=row[4],
            id_localidad_comercio=localidad,
            id_provincia_comercio=provincia,
            telefono_comercio=row[8],
            telefono2_comercio=row[9] if row[9] is not None else '',
            movil_comercio=row[10],
            mail_comercio=row[11],
            id_actividad=actividad,
            id_sucursal_comercio=sucursal,
            codigo_socio=row[14],
            id_iva_comercio=tipo_iva,
            cuit_comercio=row[16],
            ingreso_bruto=row[17]  if row[17] is not None else '',
            monto_fijo=row[18] if row[18] is not None else 0,
            estacion_servicio=row[19]  if row[19] is not None else 0,
            debito_credito=row[20]  if row[20] is not None else 1,
            acreditar_cuenta=row[21]  if row[21] is not None else 1,
            exento_ganancias=row[22]  if row[22] is not None else 0,
            mensaje=row[23]  if row[23] is not None else '',
            leido=row[24]  if row[24] is not None else 0,
            porcentaje_consumo=row[25]  if row[25] is not None else 0,
            porcentaje_retencion_ib=row[26]  if row[26] is not None else 0
        )


# Cerrar la conexión
conn.close()
