# Migrar tabla Numero de Tarjetas al modelos DJango

import os
import sys
import django
from django.db import connection
from dotenv import load_dotenv  # Importa dotenv para cargar el .env

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Agrega la ruta base del proyecto y la ruta interna del settings al PATH
sys.path.append("D:/Python/PROYECTO_TARJETA/tarjeta")

# Configura el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tarjeta.settings")
django.setup()

import pyodbc
from django.db import transaction
from apps.maestros.models.base_models import Numero

# Obtén los valores de las variables de entorno
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
username = os.getenv("SQL_USER")
password = os.getenv("SQL_PASSWORD")
driver = os.getenv("SQL_DRIVER")

# Configura la conexión con las variables del .env
conn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
)
cursor = conn.cursor()


# Query para obtener los datos de la tabla SQL Server
cursor.execute("SELECT * FROM Numeros")

def reset_modelo():
    # Elimina todos los registros del modelo `numero` en Django
    Numero.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='numero'")


# Transacción para insertar los datos de titulos en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    for row in cursor.fetchall():
        # Depuración: imprime el contenido de la fila para verificar los datos
        print(row)  # Esto imprimirá cada fila obtenida de SQL Server

        # Ajusta estos nombres de campo para que coincidan con tu modelo `Titulo` y la consulta SQL
        Numero.objects.create(
            cupon=row[1]
        )

# Cerrar la conexión
conn.close()
