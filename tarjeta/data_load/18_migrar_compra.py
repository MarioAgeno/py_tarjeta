# Migrar tabla compra al modelos DJango

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
from apps.maestros.models.base_models import Plan
from apps.maestros.models.comercio_models import Comercio
from apps.maestros.models.tarjeta_models import Tarjeta
from apps.maestros.models.compra_models import Compra

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

conusulta = '''
select tjCompras.* from tjCompras inner join tjTarjetas on tjCompras.idtarjeta = tjTarjetas.id 
	inner join tjComercios on tjCompras.idcomercio = tjComercios.id
	inner join tjPlanes on tjCompras.idplan = tjPlanes.id
'''
# Query para obtener los datos de la tabla SQL Server
cursor.execute(conusulta)

def reset_modelo():
    # Elimina todos los registros del modelo `compra` en Django
    Compra.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='compra'")


# Transacción para insertar los datos de las Compras en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    # Variable para contar los registros procesados
    contador = 0
    
    for row in cursor.fetchall():
        # Depuración: imprime el contenido de la fila para verificar los datos
        # print(row)  # Esto imprimirá cada fila obtenida de SQL Server


        plan = Plan.objects.get(id_plan=row[6])
        comercio = Comercio.objects.get(codigo_comercio=row[3])
        tarjeta = Tarjeta.objects.get(numero_tarjeta=row[4])

        if not plan: 
            print(f"No se encontró el Plan: {row[6]}")
            continue

        if not comercio: 
            print(f"No se encontró el Comercio : {row[3]}")
            continue

        if not tarjeta: 
            print(f"No se encontró la Tarjeta : {row[4]}")
            continue

        # Ajusta estos nombres de campo para que coincidan con tu modelo `compra` y la consulta SQL
        Compra.objects.create(
            id_compra=row[0],
            cupon_compra=row[1],
            fecha_compra=row[2],
            id_comercio=comercio,
            id_tarjeta=tarjeta,
            importe_compra=row[5],
            id_plan=plan,
            autorizacion=row[7],   
            procesada=row[8],
            tipo_carga=row[9],
            whatsapp=row[10]
        )

        # Incrementar el contador
        contador += 1

        # Imprimir el contador cada 1000 registros
        if contador % 1000 == 0:
            print(f"{contador} registros insertados...")

# Cerrar la conexión
conn.close()
