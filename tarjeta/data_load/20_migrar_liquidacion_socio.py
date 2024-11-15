# Migrar tabla liquidacion_socio al modelos DJango

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
from apps.maestros.models.tarjeta_models import Tarjeta
from apps.maestros.models.liquidacion_models import LiquidacionSocio

# Conexión a la base de datos SQL Server
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=PCMARIO\SQLEXPRESS;DATABASE=Tarjetas;UID=sa;PWD=maasoft')
cursor = conn.cursor()

# Query para obtener los datos de la tabla SQL Server
cursor.execute("select tjLiqSocios.* from tjLiqSocios inner join tjTarjetas on tjLiqSocios.tarjeta = tjTarjetas.id ")

def reset_modelo():
    # Elimina todos los registros del modelo `liquidacion_socio` en Django
    LiquidacionSocio.objects.all().delete()

    # Resetea el contador autoincremental del campo `id`
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='liquidacion_socio'")


# Transacción para insertar los datos de titulos en Django
with transaction.atomic():
    reset_modelo()  # Eliminar datos existentes antes de migrar

    # Variable para contar los registros procesados
    contador = 0
    for row in cursor.fetchall():
        # Depuración: imprime el contenido de la fila para verificar los datos
        # print(row)  # Esto imprimirá cada fila obtenida de SQL Server

        tarjeta = Tarjeta.objects.get(numero_tarjeta=row[1])

        if not tarjeta: 
            print(f"No se encontró La Tarjeta : {row[1]}")
            continue

        # Ajusta estos nombres de campo para que coincidan con tu modelo `liquidacion_tarejta` y la consulta SQL
        LiquidacionSocio.objects.create(
            id_liquidacion_socio=row[0],
            id_tarjeta=tarjeta,
            numero_tarjeta=row[1],
            comprobante=row[2],
            liquidacion_socio=row[3],
            cierre_anterior=row[4],
            cierre_actual=row[5],
            cierre_proximo=row[6],
            vencimiento_anterior=row[7],
            vencimiento=row[8],
            vencimiento_proximo=row[9],
            limite_tarjeta=row[10],
            saldo_anterior=row[11],
            pago_anterior=row[12],
            importe_liquidacion=row[13],
            pago_minimo=row[14],
            importe_seguro=row[15],
            importe_gasto=row[16],
            importe_interes=row[17],
            importe_punitorio=row[18],
            importe_sellado=row[19],
            importe_total=row[20],
            su_pago=row[21],
            fecha_pago=row[22] if row[22] is not None else '1900-01-01',
            sucursal_pago=row[23] if row[23] is not None else 0

        )

        # Incrementar el contador
        contador += 1

        # Imprimir el contador cada 100 registros
        if contador % 1000 == 0:
            print(f"{contador} registros insertados...")

# Cerrar la conexión
conn.close()

