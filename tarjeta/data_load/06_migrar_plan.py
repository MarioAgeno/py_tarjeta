# Migrar tabla Plan de Tarjetas al modelos DJango

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
from apps.maestros.models.base_models import Plan

# Conexión a la base de datos SQL Server
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=PCMARIO\SQLEXPRESS;DATABASE=Tarjetas;UID=sa;PWD=maasoft')
cursor = conn.cursor()

# Query para obtener los datos de la tabla SQL Server
cursor.execute("SELECT * FROM tjPlanes")

def reset_modelo():
    # Elimina todos los registros del modelo `Titulo` en Django
    Plan.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='plan'")


# Transacción para insertar los datos de titulos en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    expected_id = 1  # El ID esperado para asegurar consecutividad

    for row in cursor.fetchall():
        id = row[0]

        while expected_id < id:
            Plan.objects.create(
                estatus_plan=False,
                nombre_plan='BORRAR',
                cuotas_plan=0,
                interes_plan=0,
                costo_financiero_plan=0,
                vencimiento_plan='1900-01-01'
            )
            expected_id += 1 

        # Depuración: imprime el contenido de la fila para verificar los datos
        print(row)  # Esto imprimirá cada fila obtenida de SQL Server

        # Ajusta estos nombres de campo para que coincidan con tu modelo `Titulo` y la consulta SQL
        Plan.objects.create(
            estatus_plan=row[6],
            nombre_plan=row[1],
            cuotas_plan=row[2],
            interes_plan=row[3],
            costo_financiero_plan=row[4],
            vencimiento_plan=row[5]
        )

        expected_id += 1 

    # Eliminar los registros marcados como "BORRAR"
    # Plan.objects.filter(nombre_plan="BORRAR").delete()

# Cerrar la conexión
conn.close()
