# Migrar tabla liquidacion_comercio al modelos DJango

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
from apps.maestros.models.comercio_models import LiqudacionComercio, Comercio

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
cursor.execute("select tjLiqComercios.*, tjComercios.nombre  from tjLiqComercios inner join tjComercios on tjLiqComercios.Comercio = tjComercios.id")

def reset_modelo():
    # Elimina todos los registros del modelo `liquidacion_comercio` en Django
    LiqudacionComercio.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='liquidacion_comercio'")


# Transacción para insertar los datos de Liquidaciones a Comecios en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    # Variable para contar los registros procesados
    contador = 0
    
    for row in cursor.fetchall():
        # Depuración: imprime el contenido de la fila para verificar los datos
        # print(row)  # Esto imprimirá cada fila obtenida de SQL Server

        comercio = Comercio.objects.get(codigo_comercio=row[2])

        if not comercio: 
            print(f"No se encontró el Comercio : {row[2]}")
            continue

        # Ajusta estos nombres de campo para que coincidan con tu modelo `liquidacion_comercio` y la consulta SQL
        LiqudacionComercio.objects.create(
            liquidacion_comercio=row[1],
            id_comercio=comercio,
            fecha_liquidacion=row[3],
            importe_liquidacion=row[4],
            importe_comision=row[5],
            costo_financiero=row[6],   
            retencion_ganancias=row[7],
            retencion_iva=row[8],
            retencio_ib=row[9],
            retencion_debito_credito=row[10],
            total_liquidacion=row[11]
        )

        # Incrementar el contador
        contador += 1

        # Imprimir el contador cada 1000 registros
        if contador % 1000 == 0:
            print(f"{contador} registros insertados...")

# Cerrar la conexión
conn.close()
