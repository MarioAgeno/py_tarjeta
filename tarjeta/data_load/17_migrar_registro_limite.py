# Migrar tabla Registro_Limite de Tarjeta al  modelos DJango

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
from apps.maestros.models.tarjeta_models import Tarjeta, RegitroLimite

# Conexión a la base de datos SQL Server
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=PCMARIO\SQLEXPRESS;DATABASE=Tarjetas;UID=sa;PWD=maasoft')
cursor = conn.cursor()

# Query para obtener los datos de la tabla Tarjetas SQL Server
cursor.execute("SELECT tjRegTopes.* FROM tjRegTopes inner join tjTarjetas on tjRegTopes.idTarjeta = tjTarjetas.id ")

def reset_modelo():
    # Elimina todos los registros del modelo `Comercio` en Django
    RegitroLimite.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='registro_limite'")


# Transacción para insertar los datos de titulos en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    for row in cursor.fetchall():
        # Depuración: imprime el contenido de la fila para verificar los datos
        print(row)  # Esto imprimirá cada fila obtenida de SQL Server

        # Filtra las localidades por código postal y selecciona los campos 'id_localidad' y 'id_provincia_id'
        tarjeta = Tarjeta.objects.get(numero_tarjeta=row[0])

        if not tarjeta: 
            print(f"No se encontró la Tarjeta : {row[0]}")
            continue

        # Ajusta estos nombres de campo para que coincidan con tu modelo `RegistroLimites` y la consulta SQL
        RegitroLimite.objects.create(
            estatus_registro_limite=True,
            id_tarjeta=tarjeta,
            fecha_limite=row[1],
            maximo_limite=row[2]
        )

# Cerrar la conexión
conn.close()



