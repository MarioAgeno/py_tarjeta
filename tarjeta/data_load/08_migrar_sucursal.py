# Migrar tabla Sucursal de Tarjetas al modelos DJango

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
from apps.maestros.models.base_models import Sucursal

# Conexión a la base de datos SQL Server
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=PCMARIO\SQLEXPRESS;DATABASE=Tarjetas;UID=sa;PWD=maasoft')
cursor = conn.cursor()

# Query para obtener los datos de la tabla SQL Server
cursor.execute("SELECT * FROM tjSucursales")

def reset_modelo():
    # Elimina todos los registros del modelo `Titulo` en Django
    Sucursal.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='sucursal'")


# Transacción para insertar los datos de titulos en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    for row in cursor.fetchall():
        # Depuración: imprime el contenido de la fila para verificar los datos
        print(row)  # Esto imprimirá cada fila obtenida de SQL Server

        Sucursal.objects.create(
            estatus_sucursal=True, 
            nombre_sucursal=row[1],
            domicilio_sucursal=row[2],
            localidad_sucursal=row[3],
            codigo_postal=row[4],
            telefono=row[5],
            telefono2=row[6],
            movil=row[7],
            mail=row[8],
            ruta_archivo=row[9]
        )

# Cerrar la conexión
conn.close()
