# Migrar tabla Tarjea al  modelos DJango

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
from apps.maestros.models.tarjeta_models import Tarjeta
from apps.maestros.models.base_models import Localidad, Provincia, Titulo, Sucursal, TarjetaEstado

# Conexión a la base de datos SQL Server
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=PCMARIO\SQLEXPRESS;DATABASE=Tarjetas;UID=sa;PWD=maasoft')
cursor = conn.cursor()

# Query para obtener los datos de la tabla Tarjetas SQL Server
cursor.execute("select * from tjTarjetas")

def reset_modelo():
    # Elimina todos los registros del modelo `Comercio` en Django
    Tarjeta.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='comercio'")


# Transacción para insertar los datos de titulos en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    for row in cursor.fetchall():
        # Depuración: imprime el contenido de la fila para verificar los datos
        print(row[0], row[5])  # Esto imprimirá cada fila obtenida de SQL Server

        # Filtra las localidades por código postal y selecciona los campos 'id_localidad' y 'id_provincia_id'
        cp = row[9].strip()
        localidad = Localidad.objects.filter(codigo_postal=cp).first()
        provincia = Provincia.objects.get(id_provincia=localidad.id_provincia_id)
        titulo = Titulo.objects.get(id_titulo=row[17]+1)
        sucursal = Sucursal.objects.get(id_sucursal=row[1])
        estado = TarjetaEstado.objects.get(id_tarjeta_estado=row[18])

        # Verifica si se encontró una localidad con el código postal dado 
        if not localidad: 
            print(f"No se encontró una localidad para el código postal: {row[9]} para {row[0]} {row[5]}")
            continue

        if not provincia: 
            print(f"No se encontró una Provincia para el codigo postal: {row[9]} para {row[0]} {row[5]}")
            continue

        if not titulo: 
            print(f"No se encontró un Titulo: {row[17]} para {row[0]} {row[5]}")
            continue

        if not estado:
            print(f"No se encontró un Estado de Tarjeta : {row[18]}")
            continue

        if not sucursal:
            print(f"No se encontró la Sucursal: {row[1]} para {row[0]} {row[5]}")
            continue

        # Ajusta estos nombres de campo para que coincidan con tu modelo `Titulo` y la consulta SQL
        Tarjeta.objects.create(
            estatus_tarjeta=True,
            numero_tarjeta=row[0],
            id_sucursal_tarjeta=sucursal,
            codigo_socio=row[2],
            adicional=row[3],
            digito_verificador=row[4],
            nombre_titular=row[5],
            domicilio=row[6],
            id_localidad_tarjeta=localidad,
            id_provincia_tarjeta=provincia,
            telefono_tarjeta=row[10],
            telefono2_tarjeta=row[11] if row[11] is not None else '',
            movil_tarjeta=row[12],
            mail_tarjeta=row[13],
            nombre_garantia=row[14]   if row[14] is not None else '',
            limite_maximo_tarjeta=row[15],
            saldo_disponible=row[16],
            id_titulo=titulo if titulo is not None else 1,
            id_tarjeta_estado=estado,
            fecha_alta=row[19],
            fecha_baja=row[20] if row[20] is not None else '1900-01-01',
            vencimiento=row[21],
            liquidacion_mail=row[22] if row[22] is not None else False,
            seguro=row[23],
            observacion=row[24]  if row[24] is not None else ''
        )

# Cerrar la conexión
conn.close()
