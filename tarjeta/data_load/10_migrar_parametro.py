# Migrar tabla Parametro de Tarjetas al modelos DJango

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
from apps.maestros.models.base_models import Parametro

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

# Query para obtener los datos de la tabla Parametros de SQL Server
cursor.execute("SELECT * FROM tjParametros")

def reset_modelo():
    # Elimina todos los registros del modelo `parametro` en Django
    Parametro.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='parametro'")


# Transacción para insertar los datos de Parametros en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    for row in cursor.fetchall():
        # Depuración: imprime el contenido de la fila para verificar los datos
        print(row)  # Esto imprimirá cada fila obtenida de SQL Server
        
        # Ajusta estos nombres de campo para que coincidan con tu modelo `Titulo` y la consulta SQL
        Parametro.objects.create(
            gastos=row[0],
            tasa=row[1],
            punitorios=row[2],
            minimo=row[3],
            cierre_ultimo=row[4],
            cierre_actual=row[5],
            cierre_proximo=row[6],
            vencimiento_ultimo=row[7],
            vencimiento_actual=row[8],
            vencimiento_proximo=row[9],
            retencion_debito_credito=row[10],
            retencion_ib_general=row[11],
            retencion_ib=row[12],
            retencion_ib_minimo=row[13],
            retencion_ganancia=row[14],
            retencion_ganancia_nc=row[15],
            retencion_ganancia_minimo=row[16],
            retencion_ganancia_minimo_nc=row[17],
            retencion_iva=row[18],
            retencion_iva_estacion_servicio=row[19],
            retencion_iva_nc=row[20],
            retencion_iva_minimo=row[21],
            sello=row[22],
            seguro=row[23],
            dias_mora=row[24],
            mensaje=row[25],
            gastos_mail=row[26],
            codigo_roela=row[27]
        )

# Cerrar la conexión
conn.close()
