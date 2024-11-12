# Migrar tabla Empresa de Tarjetas al modelos DJango

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
from apps.maestros.models.base_models import Empresa

# Conexión a la base de datos SQL Server
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=PCMARIO\SQLEXPRESS;DATABASE=Tarjetas;UID=sa;PWD=maasoft')
cursor = conn.cursor()

# Query para obtener los datos de la tabla SQL Server
cursor.execute("SELECT * FROM empresa")

def reset_modelo():
    # Elimina todos los registros del modelo `Titulo` en Django
    Empresa.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='empresa'")


# Transacción para insertar los datos de titulos en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    for row in cursor.fetchall():
        # Depuración: imprime el contenido de la fila para verificar los datos
        print(row)  # Esto imprimirá cada fila obtenida de SQL Server
        
        # Ajusta estos nombres de campo para que coincidan con tu modelo `Titulo` y la consulta SQL
        Empresa.objects.create(
            estatus_empresa=True,
            razon_social=row[1],
            nombre_empresa=row[2],
            domicilio=row[3],
            localidad=row[4],
            provincia=row[5],
            codigo_postal=row[6],
            iva=row[7],
            cuit=row[8],
            ingreso_bruto=row[9] if row[9] is not None else '',
            telefono=row[10],
            telefono2=row[11],
            movil=row[12],
            mail=row[13],
            web=row[14],
            imagen=row[15]
        )

# Cerrar la conexión
conn.close()
