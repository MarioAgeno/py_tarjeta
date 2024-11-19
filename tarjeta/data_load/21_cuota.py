# Migrar tabla cuota al modelos DJango

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
from apps.maestros.models.compra_models import Operacion
from apps.maestros.models.liquidacion_models import Cuota

# Conexión a la base de datos SQL Server
# conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=HPMARIO\SQLEXPRESS;DATABASE=Tarjetas;UID=sa;PWD=maasoft')
# cursor = conn.cursor()

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
consulta = '''
select tjCuotas.* from tjCuotas inner join tjOperaciones on tjCuotas.idcompra = tjOperaciones.id
	inner join tjTarjetas on tjOperaciones.idtarjeta = tjTarjetas.id 
	inner join tjComercios on tjOperaciones.idcomercio = tjComercios.id
	inner join tjPlanes on tjOperaciones.idplan = tjPlanes.id
'''
cursor.execute(consulta)

def reset_modelo():
    # Elimina todos los registros del modelo `liquidacion_socio` en Django
    Cuota.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='cuota'")


# Transacción para insertar los datos de Cuotas de Liquidaciones a Socios en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    # Variable para contar los registros procesados
    contador = 0
    for row in cursor.fetchall():
        # Depuración: imprime el contenido de la fila para verificar los datos
        # print(row)  # Esto imprimirá cada fila obtenida de SQL Server

        compra = Operacion.objects.get(id_operacion=row[1])

        if not compra: 
            print(f"No se encontró La Compra : {row[1]}")
            continue

        # Ajusta estos nombres de campo para que coincidan con tu modelo `liquidacion_tarejta` y la consulta SQL
        Cuota.objects.create(
            id_cuota=row[0],
            id_compra=compra,
            numero_cuota=row[2],
            vencimiento_cuota=row[3],
            capital_cuota=row[4],
            interes_cuota=row[5],
            importe_cuota=row[6],
            liquidacion_socio=row[7]
        )

        # Incrementar el contador
        contador += 1

        # Imprimir el contador cada 1000 registros
        if contador % 1000 == 0:
            print(f"{contador} registros insertados...")

# Cerrar la conexión
conn.close()

