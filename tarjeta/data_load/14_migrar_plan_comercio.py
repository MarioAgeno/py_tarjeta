# Migrar tabla plan_comercio de Tarjetas al modelos DJango

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
from apps.maestros.models.comercio_models import PlanComercio, Comercio

# Conexión a la base de datos SQL Server
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=PCMARIO\SQLEXPRESS;DATABASE=Tarjetas;UID=sa;PWD=maasoft')
cursor = conn.cursor()

# Query para obtener los datos de la tabla SQL Server
cursor.execute("select tjPlanComercio.*, tjComercios.nombre  from tjPlanComercio inner join tjComercios on tjPlanComercio.idComercio = tjComercios.id")

def reset_modelo():
    # Elimina todos los registros del modelo `Plan_comercio` en Django
    PlanComercio.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='plan_comercio'")


# Transacción para insertar los datos de titulos en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    for row in cursor.fetchall():
        # Depuración: imprime el contenido de la fila para verificar los datos
        print(row)  # Esto imprimirá cada fila obtenida de SQL Server

        plan = Plan.objects.get(id_plan=row[1])
        #print(plan) # Esto imprimirá
        comercio = Comercio.objects.get(codigo_comercio=row[2])

        if not plan: 
            print(f"No se encontró el Plan: {row[1]}")
            continue

        if not comercio: 
            print(f"No se encontró el Comercio : {row[2]}")
            continue

        # Ajusta estos nombres de campo para que coincidan con tu modelo `Titulo` y la consulta SQL
        PlanComercio.objects.create(
            estatus_plan_comercio=True,
            id_plan=plan,
            id_comercio=comercio
        )

# Cerrar la conexión
conn.close()




